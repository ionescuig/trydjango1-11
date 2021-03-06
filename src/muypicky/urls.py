from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from menus.views import HomeView, HomeFeedAnonymousView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view, success_create_account


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^user-feed$', HomeFeedAnonymousView.as_view(), name='anonymous'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^success$', success_create_account, name='success'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url('^', include('django.contrib.auth.urls')),
]
