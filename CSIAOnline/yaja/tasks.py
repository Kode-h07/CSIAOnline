from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, shared_task

@shared_task
def run_reset_script():
    try:
        # Define the path to the reset.py script
        script_path = os.path.join(os.path.dirname(__file__), 'reset.py')
        print(f"Running script: {script_path}")

        # Execute the reset.py script
        exec(open(script_path).read())
    except Exception as e:
        print(f"Reset script error: {e}")