"""
URL configuration for Artsphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Artsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login),
    path('userregister', views.userregister),
    path('galleryregister', views.galleryregister),
    path('artistregister', views.artistregister),
    path('userhome', views.userhome),
    path('artisthome', views.artisthome),
    path('galleryhome', views.galleryhome),
    path('adminhome', views.adminhome),
    path('artistpost', views.artistpost),
    path('deletepost', views.deletepost),
    path('postlikes', views.postlikes),
    path('userpost', views.userpost),
    path('togglelike', views.togglelike),
    path('usercomments', views.usercomments),
    path('deletecomment', views.deletecomment),
    path('usersliked', views.usersliked),
    path('userbid', views.userbid),
    path('artistbid', views.artistbid),
    path('deletebid', views.deletebid),
    path('artistbidapprove', views.artistbidapprove),
    path('payment', views.payment),
    path('userorders', views.userorders),
    path('artistvlogs', views.artistvlogs),
    path('deletevlog', views.deletevlog),
    path('uservlogs', views.uservlogs),
    path('galleryimages', views.galleryimages),
    path('deletegalleryimage', views.deletegalleryimage),
    path('galleryevents', views.galleryevents),
    path('artistorders', views.artistorders),
    path('artistevents', views.artistevents),
    path('buyslot', views.buyslot),
    path('gallerybookings', views.gallerybookings),
    path('artistprofile', views.artistprofile),
    path('userprofile', views.userprofile),
    path('userchat', views.userchat),
    path('recieverid', views.recieverid),
    path('artistchat', views.artistchat),
    path('urecieverid', views.urecieverid),
    path('artistgallerychat', views.artistgallerychat),
    path('grecieverid', views.grecieverid),
    path('galleryuserchat', views.galleryartistchat),
    path('agrecieverid', views.agrecieverid),
    path('adminusers', views.adminusers),
    path('adminartists', views.adminartists),
    path('admingallery', views.admingalleries),
    path('toggleactive', views.toggleactive),
    path('adminreports', views.adminreports),
    path('artistcomments', views.artistcomments),
   
]
