from django.apps import AppConfig


class EgesvenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eGESVEN'

    def ready(self):
        import eGESVEN.signals
