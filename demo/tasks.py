from __future__ import absolute_import, unicode_literals
from celery import shared_task, current_task
import time

@shared_task
def add(x, y):
    return x + y

@shared_task
def increment(Limit, wait_time=0.5):
    for cnt in range(Limit):
        current_task.update_state(
                state="PROGRESS",
                meta={
                    'iteration': cnt,
                    'status': 'INCREMENTING...',
                    }
                )
        print ("Counter: {}".format(cnt))
        time.sleep(wait_time)
