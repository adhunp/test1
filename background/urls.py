from django.urls import path
from .import views

urlpatterns=[
    path('',views.adhun),
    path('athul',views.athul),
]