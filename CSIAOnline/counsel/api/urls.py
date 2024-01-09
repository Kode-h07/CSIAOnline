from django.urls import path
from .views import reservation_api, teacher_login

urlpatterns = [
    path("reservation/", reservation_api, name="reservation_api"),
    path("teacher/", teacher_login, name="teacher_login"),
]
