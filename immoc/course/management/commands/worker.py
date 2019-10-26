# Copyright 2018-present Lenovo
# Confidential and Proprietary

from django.core.management.base import BaseCommand

__all__ = ['Command']


class Command(BaseCommand):
    help = 'launch celery worker.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--log-level', default='INFO',
            choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', 'FATAL'],
            help='Logging level'
        )

        parser.add_argument(
            '--concurrency', default='4',
            help='Number of child processes processing the queue'
        )

    def handle(self, *args, **options):
        from course.main import app

        app.start(
            argv=['celery', 'worker', '-l', options['log_level'],
                  '-c', options['concurrency']]
        )
