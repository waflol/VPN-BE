from django.db import models

# Create your models here.


class Subscription(models.Model):
    class Unit(models.TextChoices):
        MONTH = "Month"
        YEAR = "Year"

    value = models.IntegerField(null=False)
    unit = models.CharField(max_length=20, choices=Unit, default=Unit.MONTH)
    discount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    final_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return "{} {}".format(self.value, self.unit)
