from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name="index"),
    # Add other app1-related paths as needed
]
