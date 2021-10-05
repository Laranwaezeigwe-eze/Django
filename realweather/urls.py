from django.urls import path

from realweather import views

urlpatterns = [
    path('', views.home)

]
