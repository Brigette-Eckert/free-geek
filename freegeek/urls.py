"""freegeek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # not working
    url(r'^$', views.home, name='home'),
    # works
    path('admin/', admin.site.urls),
    # works
    url(r'^register/?$', views.register, name='register'),
    # works
    url(r'^check_if_username_exists/$', views.check_if_username_exists, name='check_if_username_exists'),
    # not working
    url(r'^profile_page/(?P<mbr>[-\w\D]+)/?$', views.profile_page, name='profile_page'),
    # works
    url(r'login/?', views.log_in, name='login'),
    # not working
    url(r'logout/?', views.logout_view, name='logout'),

]
