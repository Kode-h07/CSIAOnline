from rest_framework import serializers
from django_app.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["time_slot", "availability", "student_name", "grade_level", "gender"]
