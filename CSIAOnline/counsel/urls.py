from django.urls import path
from . import views

urlpatterns = [
    path("", views.counsel, name="counsel"),
    path("api/", views.C)
    # Add other app1-related paths as needed
]
