# views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import (
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    DefaultMonday,
    DefaultTuesday,
    DefaultWednesday,
    DefaultThursday,
)
from .serializers import (
    MondaySerializer,
    TuesdaySerializer,
    WednesdaySerializer,
    ThursdaySerializer,
    DefaultMondaySerializer,
    DefaultTuesdaySerializer,
    DefaultWednesdaySerializer,
    DefaultThursdaySerializer,
)
from datetime import datetime
from django.contrib.auth.decorators import login_required


def get_schedule_model_for_current_day(student_id):
    current_day = datetime.now().weekday()
    try:
        if current_day == 1:
            return Tuesday.objects.get(student_id=student_id)
        elif current_day == 2:
            return Wednesday.objects.get(student_id=student_id)
        elif current_day == 3:
            return Thursday.objects.get(student_id=student_id)
        elif (
            current_day == 4 or current_day == 5 or current_day == 0 or current_day == 6
        ):
            return Monday.objects.get(student_id=student_id)
    except:
        return None


@csrf_exempt
@login_required
def yaja_view(request):
    current_student_id = request.user.student_id
    schedule = get_schedule_model_for_current_day(current_student_id)
    try:
        print(current_student_id)

        # Try to get existing Monday record
        monday_schedule, created = Monday.objects.get_or_create(
            student_id=current_student_id
        )
        if created:
            print("created monday obj")

        tuesday_schedule, created = Tuesday.objects.get_or_create(
            student_id=current_student_id
        )
        if created:
            print("created tuesday obj")

        wednesday_schedule, created = Wednesday.objects.get_or_create(
            student_id=current_student_id
        )
        if created:
            print("created weds obj")

        thursday_schedule, created = Thursday.objects.get_or_create(
            student_id=current_student_id
        )
        if created:
            print("created thursday obj")

    except Exception as e:
        print(f"An error occurred: {e}")

    if request.method == "PUT":
        data = json.loads(request.body)
        print(data)
        period1 = data.get("period1")
        period2 = data.get("period2")
        period3 = data.get("period3")
        print(period1)
        current_day = datetime.now().weekday()

        try:

            if current_day == 1:
                todayschedule = Tuesday.objects.get(student_id=current_student_id)
                serializer_class = TuesdaySerializer

            elif current_day == 2:
                todayschedule = Wednesday.objects.get(student_id=current_student_id)
                serializer_class = WednesdaySerializer

            elif current_day == 3:
                print("current_student_id in else statement")
                todayschedule = Thursday.objects.get(student_id=current_student_id)
                serializer_class = ThursdaySerializer
            else:  # Monday
                todayschedule = Monday.objects.get(student_id=current_student_id)
                serializer_class = MondaySerializer

            data = {
                "period1": period1,
                "period2": period2,
                "period3": period3,
            }
            serializer = serializer_class(todayschedule, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"status": "success"}, status=200)
            return JsonResponse(serializer.errors, status=400)

        except (
            Monday.DoesNotExist,
            Tuesday.DoesNotExist,
            Wednesday.DoesNotExist,
            Thursday.DoesNotExist,
        ):
            return JsonResponse(
                {"error": "No schedule set for the current day"}, status=404
            )

    # entire schedule update to database
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        try:
            monday = data.get("Monday")
            tuesday = data.get("Tuesday")
            wednesday = data.get("Wednesday")
            thursday = data.get("Thursday")

            default_monday, created = DefaultMonday.objects.get_or_create(
                user=request.user
            )
            default_tuesday, created = DefaultTuesday.objects.get_or_create(
                user=request.user
            )
            default_wednesday, created = DefaultWednesday.objects.get_or_create(
                user=request.user
            )
            default_thursday, created = DefaultThursday.objects.get_or_create(
                user=request.user
            )

            # Update the period data
            default_monday.period1 = monday.get("period1")
            default_monday.period2 = monday.get("period2")
            default_monday.period3 = monday.get("period3")
            default_tuesday.period1 = tuesday.get("period1")
            default_tuesday.period2 = tuesday.get("period2")
            default_tuesday.period3 = tuesday.get("period3")
            default_wednesday.period1 = wednesday.get("period1")
            default_wednesday.period2 = wednesday.get("period2")
            default_wednesday.period3 = wednesday.get("period3")
            default_thursday.period1 = thursday.get("period1")
            default_thursday.period2 = thursday.get("period2")
            default_thursday.period3 = thursday.get("period3")
            mon = {
                "period1": default_monday.get("period1"),
                "period2": default_monday.get("period2"),
                "period3": default_monday.get("period3"),
            }
            tue = {
                "period1": default_tuesday.get("period1"),
                "period2": default_tuesday.get("period2"),
                "period3": default_tuesday.get("period3"),
            }
            wed = {
                "period1": default_wednesday.get("period1"),
                "period2": default_wednesday.get("period2"),
                "period3": default_wednesday.get("period3"),
            }
            thur = {
                "period1": default_thursday.get("period1"),
                "period2": default_thursday.get("period2"),
                "period3": default_thursday.get("period3"),
            }

            # Save the changes
            Monday_serializer = DefaultMondaySerializer(
                default_monday, data=mon, partial=True
            )
            Tuesday_serializer = DefaultTuesdaySerializer(
                default_tuesday, data=tue, partial=True
            )
            Wednesday_serializer = DefaultWednesdaySerializer(
                default_wednesday, data=wed, partial=True
            )
            Thursday_serializer = DefaultThursdaySerializer(
                default_thursday, data=thur, partial=True
            )
            if (
                Monday_serializer.is_valid()
                and Tuesday_serializer.is_valid()
                and Wednesday_serializer.is_valid()
                and Thursday_serializer.is_valid()
            ):
                Monday_serializer.save()
                Tuesday_serializer.save()
                Wednesday_serializer.save()
                Thursday_serializer.save()
                return JsonResponse({"status": "echo"}, status=200)
        except (
            DefaultMonday.DoesNotExist,
            DefaultTuesday.DoesNotExist,
            DefaultWednesday.DoesNotExist,
            DefaultThursday.DoesNotExist,
        ):
            return JsonResponse({"error": "No schedule exist for student"}, status=404)

        return JsonResponse({"status": "success"}, content_type="application/json")

    elif request.method == "GET":
        if request.headers.get("Accept") == "application/json":

            # Retrieve existing schedule data
            # You need to provide the student_id here. I'm assuming you have a way to get it.
            try:
                monday_schedule = Monday.objects.get(student_id=current_student_id)
                tuesday_schedule = Tuesday.objects.get(student_id=current_student_id)
                wednesday_schedule = Wednesday.objects.get(
                    student_id=current_student_id
                )
                thursday_schedule = Thursday.objects.get(student_id=current_student_id)
            except (
                Monday.DoesNotExist,
                Tuesday.DoesNotExist,
                Wednesday.DoesNotExist,
                Thursday.DoesNotExist,
            ):
                raise ValueError("error in finding entire schedule")

            # Serialize the data
            serializer_monday = MondaySerializer(monday_schedule)
            serializer_tuesday = TuesdaySerializer(tuesday_schedule)
            serializer_wednesday = WednesdaySerializer(wednesday_schedule)
            serializer_thursday = ThursdaySerializer(thursday_schedule)

            # Combine serialized data into response
            response_data = {
                "monday": serializer_monday.data,
                "tuesday": serializer_tuesday.data,
                "wednesday": serializer_wednesday.data,
                "thursday": serializer_thursday.data,
                "action": "retrieve",
            }

            return JsonResponse(response_data, content_type="application/json")

    return render(request, "yaja.html", {"Yaja": schedule})
