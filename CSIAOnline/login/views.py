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
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        color = data.get("color")
        print(data)

        # Check if the student exists in the database
        try:
            student = Student.objects.get(
                first_name=first_name, last_name=last_name, email=email, color=color
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
