import requests
import datetime
from .models import Monday, Tuesday, Wednesday, Thursday  # Update with your app name

GOOGLE_APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbz6RqugNqN1V-2uIgt4pwLGuXCrJfGwZcC1KVPwFheCUmTz9a0bKWclJ0-iLqtJ5JEf/exec'  # Update with your Google Apps Script URL

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
            'period3': schedule.period3
        })

    response = requests.post(GOOGLE_APPS_SCRIPT_URL, json=updates)
    if response.status_code == 200:
        print("Google Sheet updated successfully.")
    else:
        print("Failed to update Google Sheet.", response.text)

if __name__ == "__main__":
    update_google_sheet()
