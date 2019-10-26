# Copyright 2018-present Lenovo
# Confidential and Proprietary

from django.core.management.base import BaseCommand

__all__ = ['Command']


class Command(BaseCommand):
    help = 'launch celery beat.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--log-level', default='INFO',
            choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', 'FATAL'],
            help='Logging level'
        )

        parser.add_argument(
            '--conf-path', default='/home/python/Desktop/lico',
            help='Store pid file and schedule db'
        )

    def handle(self, *args, **options):
        from course.main import app

        celery_conf_path = options['conf_path']
        from os import makedirs, path
        if not path.exists(celery_conf_path):
            makedirs(celery_conf_path)

        pid_file = path.join(celery_conf_path, "celerybeat.pid")
        schedule_db = path.join(celery_conf_path, "celerybeat-schedule")

        app.start(
            argv=['celery', 'beat', '-l', options['log_level'],
                  '--pidfile', pid_file, '-s', schedule_db]
        )


