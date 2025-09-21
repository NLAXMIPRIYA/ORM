from django.db import models
from django.contrib import admin

class CarInventory(models.Model): 
    car_name = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=100, primary_key=True)
    car_color = models.CharField(max_length=100)
    purchase_date = models.DateField()   
    mileage = models.IntegerField()


    def __str__(self):
        return f"{self.car_name} ({self.plate_number})"



