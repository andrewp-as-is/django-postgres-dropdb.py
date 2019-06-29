from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand
import subprocess


"""
https://www.postgresql.org/docs/current/app-dropdb.html
"""

class Command(BaseCommand):
    help = 'drop postgres database'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('alias', default='default')

    def handle(self, *args, **options):
        alias = options.get('alias')

        db_settings = settings.DATABASES[alias]
        args = ['dropdb']
        if 'USER' in db_settings:
            args+=["-O",db_settings['USER']]
        if 'HOST' in db_settings:
            args+=["-h",db_settings['HOST']]
        if 'PORT' in db_settings:
            args+=["-p",str(db_settings['PORT'])]
        # PASSWORD
        args.append(db_settings['NAME'])
        subprocess.check_call(args)
