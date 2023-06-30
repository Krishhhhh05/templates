from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_page,name="login"),
    path('index/',views.homePage,name="home"),

    path('first/',views.first),
    path('data/',views.all_data,name="all_data"),
    path('logout/',views.logout_page,name="logout"),

    path('register/',views.register,name="register"),

]