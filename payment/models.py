from django.db import models

# Create your models here.


class Subscription(models.Model):
    class Unit(models.TextChoices):
        MONTH = "Month"
        YEAR = "Year"

    value = models.IntegerField(null=False)
    unit = models.CharField(max_length=20, choices=Unit, default=Unit.MONTH)
    discount = models.IntegerField(default=0)
    final_value = models.IntegerField(null=False)

    def __str__(self):
        return "{} {}".format(self.value, self.unit)
