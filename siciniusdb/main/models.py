from django.db import models

# Create your models here.
class Person(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=2)
    job = models.CharField(max_length=30)
    added_date = models.CharField(max_length=30)
    added_by = models.CharField(max_length=30)

    def __str__(self):
        return self.fname