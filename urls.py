from django.urls import path

from calc import views

urlpatterns = [
    path('',views.home, name='home')
]