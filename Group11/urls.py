# type: ignore
"""Group11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authViews


from .views import home_page

from users.views import(
    users_list,
    Register,
    loginpage,
    logoutpage,
)

from room.views import(
    create_room,
    update_room,
    delete_room,
    
)

from blog.views import(
    create_answer,
    inside_room,
    update_blog,
    delete_blog,
    like_blog,
    like_answer,
    delete_answer,
)

admin.site.site_url = None  # Removes the 'View Site' link
admin.site.site_header = 'Corona-Overflow'

urlpatterns = [
    #reset password
    path('password-reset/', authViews.PasswordResetView.as_view(), name="password_reset"),
    path('password-reset-done/', authViews.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset-complete/', authViews.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    #Registeration
    path('users/', users_list, name='users'),
    path('', home_page ),
    path('register/', Register , name='Register'),
    path('login/', loginpage , name='loginpage'),
    path('logout/', logoutpage , name='logout'),


    #Room
    path('home/create-room/', create_room , name='create-room'),
    path('home/update-room/<str:name>/', update_room , name='update-room'),
    path('home/delete-room/<str:name>/', delete_room , name='delete-room'),
    path('home/room/<str:name>/', inside_room , name='inside-room'),


    #blog
    path('home/room/<str:name>/<int:pk>/', create_answer , name='create_answer'),
    path('home/room/update_blog/<str:name>/<int:pk>/', update_blog , name='update-blog'),
    path('home/room/delete_blog/<str:name>/<int:pk>/', delete_blog , name='delete-blog'),
    path('home/room/like/<str:name>/<int:pk>/', like_blog , name='like'),

    #answer
    path('home/room/likeanswer/<str:name>/<int:pk>/', like_answer , name='likeanswer'),
    path('home/room/delete_answer/<str:name>/<int:pk>/', delete_answer , name='delete-answer'),

    
    #home page
    path('home/', home_page , name='home'),

    #admin
    path('admin/', admin.site.urls, name='admin'),

]
