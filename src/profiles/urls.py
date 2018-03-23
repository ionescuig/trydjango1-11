from django.conf.urls import url

from .views import ProfileDetailView, ProfileUpdateView, ProfileListView

urlpatterns = [
    url(r'^all/$', ProfileListView.as_view(), name='list_all'),
    url(r'^detail-update/(?P<username>[\w-]+)/$', ProfileUpdateView.as_view(), name='detail_update'),
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]
