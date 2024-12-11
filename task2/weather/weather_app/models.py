from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.IntegerField()
    humidity = models.IntegerField()

    def __str__(self):
        return self.city