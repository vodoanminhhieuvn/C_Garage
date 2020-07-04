from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    
    def ready(self):
        import users.signals


# this is where initialize the signal for models