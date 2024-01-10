# app1/views.py
from django.shortcuts import render
from .models import Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReservationSerializer
from django.core import serializers


def counsel_view(request):
    Reservations = Reservation.objects.all()
        

    data = serializers.serialize("python", Reservation.objects.all())

    context = {
        'data': data, 
    }

    return render(request, "index.html", {"Reservations": Reservations})


@api_view(["PUT", "DELETE"])
def reservation_api(request):
    if request.method == "PUT":
        # Logic for PUT request
        time_slot = request.data.get("timeSlot")
        try:
            reservation = Reservation.objects.get(time_slot=time_slot)
        except Reservation.DoesNotExist:
            return Response(
                {"error": "Invalid time slot"}, status=status.HTTP_400_BAD_REQUEST
            )

        request.data["availability"] = False
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # Logic for DELETE request
        try:
            reservation = Reservation.objects.get(time_slot=time_slot)
        except Reservation.DoesNotExist:
            return Response(
                {"error": "Invalid time slot"}, status=status.HTTP_400_BAD_REQUEST
            )

        reservation.availability = True
        reservation.student_name = None
        reservation.grade_level = None
        reservation.gender = None
        reservation.save()

        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)


@api_view(["POST"])
def teacher_login(request):
    try:
        teacher_name = request.data.get("teacherName")
        teacher_password = request.data.get("teacherPassword")

        # Replace the following logic with your actual authentication mechanism
        if is_valid_teacher_credentials(teacher_name, teacher_password):
            # If the login is successful, you can return a JSON response with a success status
            return Response(
                {"status": "success", "message": "Teacher logged in successfully"}
            )
        else:
            # If the login fails, return a JSON response with an error status and message
            return Response(
                {
                    "status": "error",
                    "message": "Teacher login failed. Please check your name and password.",
                },
                status=401,
            )
    except Exception as e:
        # If there's an exception, return a JSON response with an error status and message
        return Response({"status": "error", "message": str(e)}, status=500)


def is_valid_teacher_credentials(teacher_name, teacher_password):
    # Replace this with your actual authentication logic
    # Example: Check against a database or another secure storage mechanism
    return teacher_name == "이수희" and teacher_password == "csiacounsel"



