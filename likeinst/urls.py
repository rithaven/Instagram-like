from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.welcome, name = 'welcome'),
    url(r'^$', views.profile, name = 'profile'),
    url(r'^$', views.timeline, name = 'timeline'), 
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^upload/profile', views.upload_profile, name = 'upload_profile')

]
