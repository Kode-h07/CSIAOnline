from django.urls import path
from yaja import views

urlpatterns = [
    path("yaja/", views.yaja_view, name="yaja"),
    path("yaja/schedule", views.yajaSchedule_view, name="schedule"),
]
