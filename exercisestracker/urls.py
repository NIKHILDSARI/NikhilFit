from django.urls import path,include
from . import views

urlpatterns=[
    path('home/', views.login_home , name ='home'),

    path('register/',views.register_user,name = 'register'),

    path('userinfo/',views.user_info,name = 'userinfo'),

    path('selectsplit/',views.select_split,name = 'selectsplit'),

    path('chestexercises/',views.chestexercises,name = 'chestexercises'),

    path('backexercises/',views.backexercises,name = 'backexercises'),

    path('userhistory/',views.user_history,name = 'userhistory'),
    
    path('logout/',views.logout_user,name = 'logout'),
    
]
