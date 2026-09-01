from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('open_signin/',views.open_signin, name='open_signin'),
    path('open_signup/',views.open_signup, name='open_signup'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signin/add_restaurent_page/',views.add_restaurent_page, name='add_restaurent_page'),
    path('signin/open_show_restaurant/',views.open_show_restaurant,name='open_show_restaurant'),
    path('add_restaurent/',views.add_restaurent,name='add_restaurent'),      
    path('add_restaurent/open_update_restaurant/<int:id>',views.open_update_restaurant,name='open_update_restaurant'),
    path('delete_restaurant/<int:id>',views.delete_restaurant,name='delete_restaurant')
]
# 12 the line == open_show_restaurant