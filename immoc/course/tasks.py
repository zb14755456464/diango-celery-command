import time

from celery import shared_task


@shared_task()
def course_task():
    print('start_cource')
    time.sleep(4)
    print('end_cource')