from django.apps import AppConfig


class DataConfig(AppConfig):
    name = 'covidFYI.data'

    def ready(self):
        
        from covidFYI.data import schedule
        # schedule.start()

        print("App ready!")
