from django.apps import AppConfig


class GarageConfig(AppConfig):
    name = 'garage'

    def ready(self):
        import garage.signals

