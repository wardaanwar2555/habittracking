from django.db import models

class User(models.Model):
  
    uemail = models.EmailField()
    upassword = models.CharField(max_length=15)

    class Meta:
        db_table = "mydatabase"


    def __str__(self):
        return self.name

class Ab(models.Model):
    habit_name = models.CharField(max_length=255)
    frequency = models.CharField(max_length=50)
    reminder_time = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.habit_name
    class Meta:
        db_table = "habit_table"
 

