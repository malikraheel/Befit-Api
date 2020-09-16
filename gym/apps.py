from django.apps import AppConfig


class GymConfig(AppConfig):
    name = 'gym'

    def ready(self):
        import gym.mysignal
