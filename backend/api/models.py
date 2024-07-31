from django.db import models

# Create your models here.
class Students(models.Model):
      first_name = models.CharField(max_length=100)
      last_name = models.CharField(max_length=100)
      age = models.IntegerField()
      gender = models.CharField(max_length=10)
      grade = models.CharField(max_length=2)
      address = models.TextField()
      contact_number = models.CharField(max_length=15)
      country = models.CharField(max_length=100)
      state = models.CharField(max_length=100)
      city = models.CharField(max_length=100)


      def __str__(self):
            return self.first_name
      
      