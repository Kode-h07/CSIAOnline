# views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import Reservation
from .serializers import ReservationSerializer
import json

@csrf_exempt
def counsel_view(request):
    if request.method == 'PUT':
        # Logic for PUT request (API request)
        data = json.loads(request.body)
        timeSlot = data.get("timeSlot")
        try:
            reservation = Reservation.objects.get(timeSlot=timeSlot)
        except Reservation.DoesNotExist:
            return Response(
                {"error": "Invalid time slot"}, status=status.HTTP_400_BAD_REQUEST
            )

        reservation.availability = False
        reservation.student_id = request.user.student_id  # Assuming user is logged in and student_id is available
        print(reservation.student_id+"this is new reserve")
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Logic for DELETE request (API request)
        data = json.loads(request.body)
        timeSlot = data.get("timeSlot")
        try:
            reservation = Reservation.objects.get(timeSlot=timeSlot, student_id=request.user.student_id)
        except Reservation.DoesNotExist:
            return Response(
                {"error": "Invalid time slot or unauthorized"}, status=status.HTTP_400_BAD_REQUEST
            )

        reservation.availability = True
        reservation.student_id = None
        reservation.save()

        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    # Logic for rendering HTML page
    Reservations = Reservation.objects.all()
    print(request.user.student_id)
    return render(request, "index.html", {"Reservations": Reservations, "current_student_id": request.user.student_id})
