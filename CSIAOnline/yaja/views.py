# views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Monday, Tuesday, Wednesday, Thursday
from .serializers import (
    MondaySerializer,
    TuesdaySerializer,
    WednesdaySerializer,
    ThursdaySerializer,
)
from datetime import datetime
import json
import pytz


def get_schedule_model_for_current_day(student_id):
    current_day = 0
    if current_day == 0:
        return Monday.objects.get(student_id=student_id)
    elif current_day == 1:
        return Tuesday.objects.get(student_id=student_id)
    elif current_day == 2:
        return Wednesday.objects.get(student_id=student_id)
    elif current_day == 3:
        return Thursday.objects.get(student_id=student_id)
    else:
        raise ValueError("Unsupported day") 

@csrf_exempt
def yaja_view(request):
    current_student_id = request.user.student_id
    currentDay_schedule = get_schedule_model_for_current_day(current_student_id)
    if request.method == "PUT":
        # if 시간을 통해서 무슨 요일인지
        data = json.loads(request.body)
        print(data)
        period1 = data.get("period1")
        period2 = data.get("period2")
        period3 = data.get("period3")
        #current_day = datetime.now().weekday()
        current_day = 0

        try:
            if current_day == 0:  # Monday
                schedule = Monday.objects.get(student_id=current_student_id)
                serializer = MondaySerializer(schedule)
                currentDay_schedule = Monday.objects.get(student_id=request.user.student_id)

            elif current_day == 1:
                schedule = Tuesday.objects.get(student_id=current_student_id)
                serializer = TuesdaySerializer(schedule)
                currentDay_schedule = Tuesday.objects.get(student_id=request.user.student_id)

            elif current_day == 2:
                schedule = Wednesday.objects.get(student_id=current_student_id)
                serializer = WednesdaySerializer(schedule)
                currentDay_schedule = Wednesday.objects.get(student_id=request.user.student_id)

            elif current_day == 3:
                schedule = Thursday.objects.get(student_id=current_student_id)
                serializer = ThursdaySerializer(schedule)
                currentDay_schedule = Thursday.objects.get(student_id=request.user.student_id)

            else:
                return JsonResponse({"error": "Unsupported day"})
            
            currentDay_schedule.period1 = period1
            currentDay_schedule.period2 = period2
            currentDay_schedule.period3 = period3
            currentDay_schedule.save()
            return JsonResponse(serializer.data, content_type="application/json")
        
        except Monday.DoesNotExist:
            return JsonResponse({"error": "No schedule set for Monday"})

        except Tuesday.DoesNotExist:
            return JsonResponse({"error": "No schedule set for Tuesday"})

        except Wednesday.DoesNotExist:
            return JsonResponse({"error": "No schedule set for Wednesday"})

        except Thursday.DoesNotExist:
            return JsonResponse({"error": "No schedule set for Thursday"})
        
    return render(request, "yaja.html", {"Yaja": currentDay_schedule})


@csrf_exempt
def yajaSchedule_view(request):
    current_student_id = request.user.student_id
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)

        monday = data.get("monday")
        tuesday = data.get("tuesday")
        wednesday = data.get("wednesday")
        thursday = data.get("thursday")

        current_student_id = request.user.student_id

        try:
            # Try to get existing records
            monday_schedule = Monday.objects.get(student_id=current_student_id)
            tuesday_schedule = Tuesday.objects.get(student_id=current_student_id)
            wednesday_schedule = Wednesday.objects.get(student_id=current_student_id)
            thursday_schedule = Thursday.objects.get(student_id=current_student_id)
        except (
            Monday.DoesNotExist,
            Tuesday.DoesNotExist,
            Wednesday.DoesNotExist,
            Thursday.DoesNotExist,
        ):
            # Create new records if they don't exist
            monday_schedule = Monday.objects.create(student_id=current_student_id)
            tuesday_schedule = Tuesday.objects.create(student_id=current_student_id)
            wednesday_schedule = Wednesday.objects.create(student_id=current_student_id)
            thursday_schedule = Thursday.objects.create(student_id=current_student_id)

        # Update the period data
        monday_schedule.period1 = monday.get("period1")
        tuesday_schedule.period1 = tuesday.get("period1")
        wednesday_schedule.period1 = wednesday.get("period1")
        thursday_schedule.period1 = thursday.get("period1")
        monday_schedule.period2 = monday.get("period2")
        tuesday_schedule.period2 = tuesday.get("period2")
        wednesday_schedule.period2 = wednesday.get("period2")
        thursday_schedule.period2 = thursday.get("period2")
        monday_schedule.period3 = monday.get("period3")
        tuesday_schedule.period3 = tuesday.get("period3")
        wednesday_schedule.period3 = wednesday.get("period3")
        thursday_schedule.period3 = thursday.get("period3")

        # Save the changes
        monday_schedule.save()
        tuesday_schedule.save()
        wednesday_schedule.save()
        thursday_schedule.save()

        # Serialize the data
        serializer_monday = MondaySerializer(monday_schedule)
        serializer_tuesday = TuesdaySerializer(tuesday_schedule)
        serializer_wednesday = WednesdaySerializer(wednesday_schedule)
        serializer_thursday = ThursdaySerializer(thursday_schedule)

        # Combine the serialized data into a response
        response_data = {
            "monday": serializer_monday.data,
            "tuesday": serializer_tuesday.data,
            "wednesday": serializer_wednesday.data,
            "thursday": serializer_thursday.data,
            "status": "success",
        }

        return JsonResponse(response_data, content_type="application/json")
    try:
        monday_schedule = Monday.objects.get(student_id=current_student_id)
        tuesday_schedule = Tuesday.objects.get(student_id=current_student_id)
        wednesday_schedule = Wednesday.objects.get(student_id=current_student_id)
        thursday_schedule = Thursday.objects.get(student_id=current_student_id)
    except:

        monday_schedule = None
        tuesday_schedule = None
        wednesday_schedule = None
        thursday_schedule = None

        monday_schedule = {"period1":"None", "period2":"None", "period3":"None"}
        tuesday_schedule = {"period1":"None", "period2":"None", "period3":"None"}
        wednesday_schedule = {"period1":"None", "period2":"None", "period3":"None"}
        thursday_schedule = {"period1":"None", "period2":"None", "period3":"None"}
        

    # 만약 이미 있는거 부분수정하고 싶은거면 현재거를 보여지는 폼 디폴트로 설정할 수있나?
    # 아님 걍 하라 그러고
    return render(
        request,
        "schedule.html",

        {
            "current_schedule": {
                "monday": monday_schedule,
                "tuesday": tuesday_schedule,
                "wednesday": wednesday_schedule,
                "thursday": thursday_schedule,
            }
        },

        {"schedule" :{
            "monday": monday_schedule,
            "tuesday": tuesday_schedule,
            "wednesday": wednesday_schedule,
            "thursday": thursday_schedule,
        }},

    )