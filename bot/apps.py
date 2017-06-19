from django.apps import AppConfig
from watson import search as watson

class BotConfig(AppConfig):
    name = 'bot'

    def ready(self):
        IA = self.get_model("IA")
        watson.register(IA)
