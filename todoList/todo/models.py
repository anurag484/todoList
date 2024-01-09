from django.db import models

# Create your models here.
class taskModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    # add a user field that links to the user model
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # add a completed field that is a boolean
    completed = models.BooleanField(default=False)
    # add a created field that is a date
    created = models.DateTimeField(auto_now_add=True)
    # add a due date field that is a date
    due_date = models.DateField()
    # add a priority field that is a number
    priority = models.IntegerField(default=1)
    # add a category field that is a string
    category = models.CharField(max_length=122)
    # add a description field that is a string
    description = models.CharField(max_length=122)


    def __str__(self):
        return self.name