from django.shortcuts import render


def home_view(request):
    # Your logic to aggregate data or render templates goes here
    print(request.user.student_id)
    return render(request, "home.html")
