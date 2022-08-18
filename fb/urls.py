from django.urls import path
from .import views

urlpatterns=[
    path('facebook',views.fb),
    path('signup',views.signup),
    path('home',views.home),
    
]