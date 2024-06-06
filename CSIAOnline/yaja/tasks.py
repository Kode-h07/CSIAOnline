from celery import shared_task
import subprocess

@shared_task
def run_reset_script():
    # Assuming reset.py is in the same directory as tasks.py
    script_path = 'reset.py'
    subprocess.run(['python', script_path])