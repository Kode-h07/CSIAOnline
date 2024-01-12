# views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Monday, Tuesday, Wednesday, Thursday
from .serializers import MondaySerializer, TuesdaySerializer, WednesdaySerializer, ThursdaySerializer
import json
from django.utils import timezone
import pytz
import datetime

@csrf_exempt
def yaja_view(request):
    if request.method == 'PUT':
        #if 시간을 통해서 무슨 요일인지 
        data = json.loads(request.body)
        print(data)
        period1 = data.get("period1")
        period2 = data.get("period2")
        period3 = data.get("period3")
        current_student_id = request.user.student_id
        try:
            schedule = Monday.objects.get(student_id = current_student_id)
            print(schedule)
        except Monday.DoesNotExist:
            print("not existing shit")
            return JsonResponse(
                {"error": "No schedule set"}
            )
        schedule.period1 = period1
        schedule.period2 = period2
        schedule.period3 = period3
        schedule.save()
        serializer = MondaySerializer(schedule)
        return JsonResponse(serializer.data, content_type="application/json")
    
    Monday_schedule = Monday.objects.get(student_id = request.user.student_id)
    # current_day = get_day_of_week()  # Get the current day of the week
    # print(current_day)
    return render(request, "yaja.html", {"Yaja": Monday_schedule})

    


# def get_day_of_week():

#     korea_timezone = pytz.timezone('America/Mexico_City')
#     current_datetime = datetime.datetime.now(korea_timezone)
#     # Get the current date and time in the UTC timezone
#     current_datetime = pytz.timezone.now()

#     # Get the day of the week as an integer (Monday is 0, Sunday is 6)
#     day_of_week_int = current_datetime.weekday()

#     # Map the integer to the corresponding day name
#     days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     day_of_week_name = days_of_week[day_of_week_int]

#     return f"The current day of the week is: {day_of_week_name}"

# Call the function and print the result

    



        