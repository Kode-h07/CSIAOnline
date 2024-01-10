from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login(request):
    if request.method == "POST":
        # Get data from the form
        data = json.loads(request.body.decode('utf-8'))
        student_id = data.get("student_id")
        email = data.get("email")
        password = data.get("password")
        print(data)

        # Check if the student exists in the database
        try:
            student = Student.objects.get(
                student_id=student_id, email=email, password=password
            )
            # Redirect to the home page if the student is found
            return JsonResponse({"status":"success"})
        except Student.DoesNotExist:
            # If the student is not found, return an error message
            return JsonResponse(
                {"error": "Invalid login credentials. Please check your inputs."},
                status=400,
            )

    return render(request, "login/login.html")
