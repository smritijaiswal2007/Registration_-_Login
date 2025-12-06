from django.db import models


# Create your models here.
class Student(models.Model):

    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Detail=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='image/')
    Password = models.CharField(max_length=100)


    # def _str_(self):
    #     return str(self.Contact) + self.Name + self.Email

    def _str_(self):
        return self.Name