from celery_app import add

#send task to worker with delay()
add.delay(4, 4)