from django.db import models

class Squirrel(models.Model):

    Latitude = models.FloatField(blank=False,)
    Longitude = models.FloatField(blank=False,)
    Unique_Squirrel_ID = models.CharField(max_length=1000,blank=False, primary_key=True,)
    Shift = models.CharField(max_length=1000, null=True,blank=False,)
    Date = models.DateField(null=True,blank=False,)
    Age = models.CharField(max_length=1000, null=True,)
    Primary_Fur_Color = models.CharField(max_length=1000, null=True,blank=True,)
    Location = models.CharField(max_length=1000, null=True,blank=True,)
    Specific_Location = models.CharField(max_length=1000, null=True,blank=True,)
    Running = models.BooleanField(blank=True,)
    Chasing = models.BooleanField(blank=True,)
    Climbing = models.BooleanField(blank=True,)
    Eating = models.BooleanField(blank=True,)
    Foraging = models.BooleanField(blank=True,)
    Other_Activities = models.CharField(max_length=1000, null=True, blank=True,)
    Kuks = models.BooleanField(blank=True,)
    Quaas = models.BooleanField(blank=True,)
    Moans = models.BooleanField(blank=True,)
    Tail_Flags = models.BooleanField(blank=True,)
    Tail_Twitches = models.BooleanField(blank=True,)
    Approaches = models.BooleanField(blank=True,)
    Indifferent = models.BooleanField(blank=True,)
    Runs_From = models.BooleanField(blank=True,)

    def __str__(self):
        return self.Unique_Squirrel_ID
# Create your models here.
