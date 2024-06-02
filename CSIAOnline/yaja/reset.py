# myapp/management/commands/reset_schedules.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
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


class Command(BaseCommand):
    help = "Resets user schedules to default values every Friday"

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        if today.weekday() == 4:  # Check if today is Friday
            for user in User.objects.all():
                try:
                    default_monday = DefaultMonday.objects.get(user=user)
                    default_tuesday = DefaultTuesday.objects.get(user=user)
                    default_wednesday = DefaultWednesday.objects.get(user=user)
                    default_thursday = DefaultThursday.objects.get(user=user)

                    Monday.objects.filter(student_id=user.student_id).update(
                        period1=default_monday.period1,
                        period2=default_monday.period2,
                        period3=default_monday.period3,
                    )
                    Tuesday.objects.filter(student_id=user.student_id).update(
                        period1=default_tuesday.period1,
                        period2=default_tuesday.period2,
                        period3=default_tuesday.period3,
                    )
                    Wednesday.objects.filter(student_id=user.student_id).update(
                        period1=default_wednesday.period1,
                        period2=default_wednesday.period2,
                        period3=default_wednesday.period3,
                    )
                    Thursday.objects.filter(student_id=user.student_id).update(
                        period1=default_thursday.period1,
                        period2=default_thursday.period2,
                        period3=default_thursday.period3,
                    )
                except (
                    DefaultMonday.DoesNotExist,
                    DefaultTuesday.DoesNotExist,
                    DefaultWednesday.DoesNotExist,
                    DefaultThursday.DoesNotExist,
                ):
                    continue

            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully reset user schedules to default values"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING("Today is not Friday. No reset performed.")
            )
