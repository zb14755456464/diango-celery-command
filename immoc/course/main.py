# Copyright 2018-present Lenovo
# Confidential and Proprietary


from celery import Celery


app = Celery(__name__)
app.config_from_object('django.conf:settings')
