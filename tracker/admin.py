from django.contrib import admin
from .models import Category, Expense

# Register your models here.

# this registers the models to the admin site and creates 
# a full CRUD interface for these tables.

admin.site.register(Category)
admin.site.register(Expense)

