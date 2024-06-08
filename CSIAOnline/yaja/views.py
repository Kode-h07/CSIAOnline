# views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core.exceptions import ObjectDoesNotExist
from .reset import reset_schedules
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


def get_schedule_model_for_current_day(student_id):
    current_day = datetime.now().weekday()
    try:
        if current_day == 1:
            return Tuesday.objects.get(student_id=student_id)
        elif current_day == 2:
            return Wednesday.objects.get(student_id=student_id)
        elif current_day == 3:
            return Thursday.objects.get(student_id=student_id)
        elif (current_day == 4 or current_day == 5 or current_day == 0 or current_day == 6):  
            print("retrieved tody: monday schedule")
            return Monday.objects.get(student_id=student_id)
    except:
        return None


@csrf_exempt
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
        try:
            monday_data = data.get("Monday")
            try:
                monday = Monday.objects.get(student_id=current_student_id)
            except ObjectDoesNotExist:
                monday = Monday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
            monday.period1 = monday_data.get("period1")
            monday.period2 = monday_data.get("period2")
            monday.period3 = monday_data.get("period3")
            monday.save()

            tuesday_data = data.get("Tuesday")
            try:
                tuesday = Tuesday.objects.get(student_id=current_student_id)
            except ObjectDoesNotExist:
                tuesday = Tuesday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
            tuesday.period1 = tuesday_data.get("period1")
            tuesday.period2 = tuesday_data.get("period2")
            tuesday.period3 = tuesday_data.get("period3")
            tuesday.save()

            wednesday_data = data.get("Wednesday")
            try:
                wednesday = Wednesday.objects.get(student_id=current_student_id)
            except ObjectDoesNotExist:
                wednesday = Wednesday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
            wednesday.period1 = wednesday_data.get("period1")
            wednesday.period2 = wednesday_data.get("period2")
            wednesday.period3 = wednesday_data.get("period3")
            wednesday.save()

            thursday_data = data.get("Thursday")
            try:
                thursday = Thursday.objects.get(student_id=current_student_id)
            except ObjectDoesNotExist:
                thursday = Thursday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
            thursday.period1 = thursday_data.get("period1")
            thursday.period2 = thursday_data.get("period2")
            thursday.period3 = thursday_data.get("period3")
            thursday.save()

            print("Schedule updated successfully")
            return JsonResponse(
                {"status": "success", "student_id": current_student_id}, status=200
            )
        except (
            Monday.DoesNotExist,
            Tuesday.DoesNotExist,
            Wednesday.DoesNotExist,
            Thursday.DoesNotExist,
        ):
            return JsonResponse({"error": "No schedule exists for student"}, status=404)

    # entire schedule update to database
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        try:
            monday = data.get("Monday")
            tuesday = data.get("Tuesday")
            wednesday = data.get("Wednesday")
            thursday = data.get("Thursday")

            try:
                default_monday = DefaultMonday.objects.get(
                    student_id=current_student_id
                )
            except ObjectDoesNotExist:
                default_monday = DefaultMonday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )

            try:
                default_tuesday = DefaultTuesday.objects.get(
                    student_id=current_student_id
                )
            except ObjectDoesNotExist:
                default_tuesday = DefaultTuesday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )

            try:
                default_wednesday = DefaultWednesday.objects.get(
                    student_id=current_student_id
                )
            except ObjectDoesNotExist:
                default_wednesday = DefaultWednesday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )

            try:
                default_thursday = DefaultThursday.objects.get(
                    student_id=current_student_id
                )
            except ObjectDoesNotExist:
                default_thursday = DefaultThursday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
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
                "period1": default_monday.period1,
                "period2": default_monday.period2,
                "period3": default_monday.period3,
            }
            tue = {
                "period1": default_tuesday.period1,
                "period2": default_tuesday.period2,
                "period3": default_tuesday.period3,
            }
            wed = {
                "period1": default_wednesday.period1,
                "period2": default_wednesday.period2,
                "period3": default_wednesday.period3,
            }
            thur = {
                "period1": default_thursday.period1,
                "period2": default_thursday.period2,
                "period3": default_thursday.period3,
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
                print("before reset")
                reset_schedules(current_student_id)
                print("after reset")
                return JsonResponse(
                    {"status": "echo", "student_id": current_student_id}, status=200
                )
        except (
            DefaultMonday.DoesNotExist,
            DefaultTuesday.DoesNotExist,
            DefaultWednesday.DoesNotExist,
            DefaultThursday.DoesNotExist,
        ):
            return JsonResponse({"error": "No schedule exist for student"}, status=404)

    elif request.method == "GET":
        if request.headers.get("X-Schedule-Type") == "default":
            print("GET default schedule backend success reached")

            # Retrieve existing schedule data
            # You need to provide the student_id here. I'm assuming you have a way to get it.
            try:
                monday_schedule = DefaultMonday.objects.get(
                    student_id=current_student_id
                )
                tuesday_schedule = DefaultTuesday.objects.get(
                    student_id=current_student_id
                )
                wednesday_schedule = DefaultWednesday.objects.get(
                    student_id=current_student_id
                )
                thursday_schedule = DefaultThursday.objects.get(
                    student_id=current_student_id
                )
                print("Monday schedule retrieved")
            except:
                print("Monday schedule does not exist, creating default schedules")
                monday_schedule = DefaultMonday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
                tuesday_schedule = DefaultTuesday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
                wednesday_schedule = DefaultWednesday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
                thursday_schedule = DefaultThursday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )

            # Serialize the data
            serializer_monday = DefaultMondaySerializer(monday_schedule)
            serializer_tuesday = DefaultTuesdaySerializer(tuesday_schedule)
            serializer_wednesday = DefaultWednesdaySerializer(wednesday_schedule)
            serializer_thursday = DefaultThursdaySerializer(thursday_schedule)

            print(serializer_monday.data)
            # Combine serialized data into response
            response_data = {
                "monday": serializer_monday.data,
                "tuesday": serializer_tuesday.data,
                "wednesday": serializer_wednesday.data,
                "thursday": serializer_thursday.data,
                "action": "retrieve",
            }

            return JsonResponse(response_data)
        elif request.headers.get("X-Schedule-Type") == "current":
            print("GET current schedule backend success reached")

            # Retrieve existing schedule data
            try:
                monday_schedule = Monday.objects.get(student_id=current_student_id)
                tuesday_schedule = Tuesday.objects.get(student_id=current_student_id)
                wednesday_schedule = Wednesday.objects.get(student_id=current_student_id)
                thursday_schedule = Thursday.objects.get(student_id=current_student_id)
                print("All schedule retrieved")

                # Check and assign "yaja" if any period is null
                if not monday_schedule.period1: monday_schedule.period1 = "야자"
                if not monday_schedule.period2: monday_schedule.period2 = "야자"
                if not monday_schedule.period3: monday_schedule.period3 = "야자"
                if not tuesday_schedule.period1: tuesday_schedule.period1 = "야자"
                if not tuesday_schedule.period2: tuesday_schedule.period2 = "야자"
                if not tuesday_schedule.period3: tuesday_schedule.period3 = "야자"
                if not wednesday_schedule.period1: wednesday_schedule.period1 = "야자"
                if not wednesday_schedule.period2: wednesday_schedule.period2 = "야자"
                if not wednesday_schedule.period3: wednesday_schedule.period3 = "야자"
                if not thursday_schedule.period1: thursday_schedule.period1 = "야자"
                if not thursday_schedule.period2: thursday_schedule.period2 = "야자"
                if not thursday_schedule.period3: thursday_schedule.period3 = "야자"

                # Save the changes
                monday_schedule.save()
                tuesday_schedule.save()
                wednesday_schedule.save()
                thursday_schedule.save()
            except Monday.DoesNotExist:
                print("Monday schedule does not exist, creating default schedule")
                monday_schedule = Monday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
            except Tuesday.DoesNotExist:
                print("Tuesday schedule does not exist, creating default schedule")
                tuesday_schedule = Tuesday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
            except Wednesday.DoesNotExist:
                print("Wednesday schedule does not exist, creating default schedule")
                wednesday_schedule = Wednesday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
            except Thursday.DoesNotExist:
                print("Thursday schedule does not exist, creating default schedule")
                thursday_schedule = Thursday.objects.create(
                    student_id=current_student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )

            # Serialize the data
            serializer_monday = MondaySerializer(monday_schedule)
            serializer_tuesday = TuesdaySerializer(tuesday_schedule)
            serializer_wednesday = WednesdaySerializer(wednesday_schedule)
            serializer_thursday = ThursdaySerializer(thursday_schedule)

            print(serializer_monday.data)
            # Combine serialized data into response
            response_data = {
                "monday": serializer_monday.data,
                "tuesday": serializer_tuesday.data,
                "wednesday": serializer_wednesday.data,
                "thursday": serializer_thursday.data,
                "action": "retrieve",
            }

            return JsonResponse(response_data)

    return render(request, "yaja.html", {"Yaja": schedule})
