from django.urls import path
from . import views
urlpatterns = [
    path('',views.homePage),
    path('first/',views.first),
    path('data/',views.all_data,name="all_data"),

]