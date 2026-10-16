"""
URL configuration for socialmedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from social_media_app.views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

# router=DefaultRouter()

# router.register('post',PostView,basename="post")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',SignupView.as_view()),
    path('token',obtain_auth_token),
    path('feed',Postcreate.as_view()),
    path('postview/<int:pk>',PostView.as_view()),
    path('comment/<int:pk>',CommentPost.as_view()),
    path('user/<int:pk>',UserRetrieveView.as_view()),
    path('comment-delete/<int:pk>',CommentDelete.as_view()),
    path('like/<int:pk>',LikeView.as_view()),
    path('unlike/<int:pk>',UnLike.as_view())
]

