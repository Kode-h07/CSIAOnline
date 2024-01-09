from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Student


def login(request):
    if request.method == "POST":
        # Get data from the form
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        color = request.POST.get("color")

        # Check if the student exists in the database
        try:
            student = Student.objects.get(
                first_name=first_name, last_name=last_name, email=email, color=color
            )
            # Redirect to the home page if the student is found
            return redirect("home")
        except Student.DoesNotExist:
            # If the student is not found, return an error message
            return JsonResponse(
                {"error": "Invalid login credentials. Please check your inputs."},
                status=400,
            )

    return render(request, "login/login.html")
