from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField("Name", max_length=255)
    email = models.EmailField()
    document = models.CharField("Document", max_length=255)
    phone = models.CharField(max_length=10)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name