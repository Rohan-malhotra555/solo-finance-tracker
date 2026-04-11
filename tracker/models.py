from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class TrackerUser(AbstractUser):

    # We can either define any new field we want (AbstractUser itself gives
    # username, firstname, lastname, password and email field) else we give 'pass'.

    def __str__(self):
        return self.username
    
class Category(models.Model):

    name = models.CharField(max_length=100)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "categories")

    def __str__(self):

        return self.name


class Expense(models.Model):

    # Decimal field is used as Float causes decimal pointer issues while doing math.
    amount = models.DecimalField(max_digits=10, decimal_places=2) 

    description = models.CharField(max_length=255)

    # Kept this without auto_now_add because user can add expenses of previous dates.
    # so kept empty for manual selection.
    date = models.DateField()

    # IMPORTANT: We can have same related name for foreign key fields that 
    # point to different classes but NOT for the fields that point to the same class.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="expenses")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="expenses")


    def __str__(self):

        return self.description




