from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Wating for DB Connection....")

        is_db_connected = None

        while not is_db_connected:
            try:
                is_db_connected = connections["default"]
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Connection Trying to connect..........")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("PostgreSQL Connections Success"))
