'''Used to connecting our hour manager server to the SQL DB'''
from django.db import models

# Create your models here.
class HourModel(models.Model):
    '''A model for holding hours'''
    first_name = models.CharField(max_length=15, help_text="Your first name.")
    last_name = models.CharField(max_length=20, help_text="Your last name.")
    date = models.DateField()
    start_time = models.TimeField(help_text="In military time.")
    end_time = models.TimeField(help_text="In military time.")
    reason = models.CharField(max_length=120, help_text="The reason you need this shift covered.")

    def __str__(self):
        '''Returns a string representation of the entry'''
        return "{} {} | {}:{}".format(self.first_name, self.last_name, self.date, self.start_time)

class hour_history(models.Model):
    cover_first = models.CharField(max_length=15)
    cover_last = models.CharField(max_length=20)
    coveree_first = models.CharField(max_length=15)
    coveree_last = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()