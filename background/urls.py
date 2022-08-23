from django.urls import path
from .import views

urlpatterns=[
    path('adhun',views.adhun),
    path('athul',views.athul),
]