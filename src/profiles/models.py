from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.template.loader import render_to_string

from .utils import code_generator

User = settings.AUTH_USER_MODEL


class ProfileManager(models.Manager):
    def toggle_follow(self, request_user, username_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = request_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_, is_following


class Profile(models.Model):
    user            = models.OneToOneField(User)
    followers       = models.ManyToManyField(User, related_name='is_following', blank=True)
    # following     = models.ManyToManyField(User, related_name='following', blank=True)
    activation_key  = models.CharField(max_length=120, blank=True, null=True)
    activated       = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activation_email(self, base_url):
        print("> Activation")
        if not self.activated:
            self.activation_key = code_generator()
            self.save()

            activate_url = base_url + reverse('activate', kwargs={"code": self.activation_key})
            # print(activate_url)

            template_name = 'profiles/html_message.html'
            context = {'user': self.user, 'activate_url': activate_url}
            html_content = render_to_string(template_name, context)

            subject = 'Activate account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'Activate your account here'
            recipient_list = [self.user.email]

            # print(html_content)
            # sent_mail = False
            # Uncomment to send email. After setting the right email in base.py
            sent_mail = send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
                html_message=html_content
            )
            return sent_mail


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        default_user_profile.followers.add(instance)
        profile.followers.add(default_user_profile.user)
        profile.followers.add(2)


post_save.connect(post_save_user_receiver, sender=User)
