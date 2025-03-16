from django.db import models

# Create your models here.
class Subscription(models.Model):
    class Unit(models.TextChoices):
        YEAR = 'Year'
        MONTH = 'Month'
    value = models.IntegerField(null=False)
    unit = models.CharField(choices=Unit, default=Unit.MONTH, max_length=20)
    discount = models.IntegerField(default=0)
    

class Invoice(models.Model):
    pass


class Payment(models.Model):
    pass