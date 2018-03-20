from django.conf.urls import url

from .views import ProfileDetailView, ProfileListView

urlpatterns = [
    url(r'^all/$', ProfileListView.as_view(), name='list_all'),
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]
