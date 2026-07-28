from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Base'

    def ready(self):
        # Yeh code automatically startup par tables migrate kar dega agar missing huiin
        try:
            from django.core.management import call_command
            call_command('migrate', interactive=False)
        except Exception:
            pass    