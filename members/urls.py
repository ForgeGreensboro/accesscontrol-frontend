from django.conf.urls import url, include

from . import views

app_name = 'members'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
