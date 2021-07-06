from django.db import models
from django.contrib.auth.models import User
from django.http import request

# Create your models here.
class Image(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/%y')

    def __str__(self):
        return self.caption

class Profile(models.Model):
    # user_id = models.AutoField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, default="")
    age = models.IntegerField()
    pic = models.URLField()
    # pic = models.ForeignKey(Image, on_delete=models.CASCADE)
    # pic = models.ImageField()
    # pic = models.ImageField(upload_to="home/uploaded-pics")
    phone = models.CharField(max_length=15, default="")
    date_of_birth = models.DateField(default="")
    city = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=150, default="")
    father_name = models.CharField(max_length=100, default="")
    mother_name = models.CharField(max_length=100, default="")
    father_phone = models.CharField(max_length=15, default="")
    work_address = models.CharField(max_length=150, default="")
    occupation = models.CharField(max_length=100, default="")
    salary = models.IntegerField(default="")
    qualification = models.CharField(max_length=500, default="")
    hobby = models.CharField(max_length=150, default="")
    caste = models.CharField(max_length=100, default="")
    religion = models.CharField(max_length=100, default="")
    family_type = models.CharField(max_length=100, default="", help_text="small/big/joint")
    
    def __str__(self):
        return self.user.username
