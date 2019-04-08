from django.db import models


class Location(models.Model):
    street = models.CharField(max_length=200)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

class Reminder(models.Model):
    reminder_text = models.CharField(max_length=200)
    reminder_date = models.DateTimeField('date')
    reminder_location = models.ForeignKey(Location, on_delete=models.CASCADE)



