import requests
import datetime
from ...models import Monday, Tuesday, Wednesday, Thursday  # Update with your app name
from django.core.management.base import BaseCommand

GOOGLE_APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyGpG1culjD-kgrqO5MdJSy2rZpWpxPUv_9RcjkoS2IgmVonnV8PBUayTTdwgJz-Dlp/exec'
def fetch_schedule():
    day_of_week = datetime.datetime.today().weekday()
    if (day_of_week  == 0 or day_of_week == 4 or day_of_week == 5 or day_of_week==6):
        schedules = Monday.objects.all()
    elif day_of_week == 1:
        schedules = Tuesday.objects.all()
    elif day_of_week == 2:
        schedules = Wednesday.objects.all()
    elif day_of_week == 3:
        schedules = Thursday.objects.all()
    else:
        return None
    return schedules

def update_google_sheet():
    schedules = fetch_schedule()
    if not schedules:
        print("No schedules to update for today.")
        return
    
    updates = []
    for schedule in schedules:

        updates.append({
            'student_id': schedule.student_id,
            'period1': schedule.period1,
            'period2': schedule.period2,
            'period3': schedule.period3,
        })
    print(updates)

    response = requests.post(GOOGLE_APPS_SCRIPT_URL, json=updates)
    if response.status_code == 200:
        print(response)
        print("Google Sheet updated successfully.")
    else:
        print("Failed to update Google Sheet.", response.text)


class Command(BaseCommand):
    print("command called on update_google_sheet.py")
    help = "Resets user schedules to default values every Friday"

    def handle(self, *args, **kwargs):
        update_google_sheet()