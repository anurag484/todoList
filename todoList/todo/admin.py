from django.contrib import admin

# Register your models here.
from .models import taskModel

admin.site.register(taskModel)