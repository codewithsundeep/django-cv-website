from django.db import models
from django.utils import timezone

# Create your models here.
class personal_info(models.Model):
    Name = models.CharField(max_length=25,default="Lorem ipsum")
    Title = models.CharField(max_length=25,default="Web developer")
    Address = models.CharField(max_length=50,default="Sikkim India")
    Email = models.EmailField(default="example@youremail.com")
    Phone = models.CharField(max_length=15,default="+911234567890")
    Image = models.ImageField(upload_to="static/images")
    
class Skills(models.Model):
    Skill = models.CharField(max_length=50,default="Python")
    Percent = models.IntegerField()

class Languages(models.Model):
    Language = models.CharField(max_length=25,default="English")
    Percent = models.IntegerField()

class Current_Work(models.Model):
    Title = models.CharField(max_length=50,default="Web developer")
    Started_at = models.CharField(max_length=10,default="Jan 2021")
    Description = models.TextField(default="Lorem ipsum dolor sit amet. Praesentium magnam consectetur vel in deserunt aspernatur est reprehenderit sunt hic. Nulla tempora soluta ea et odio, unde doloremque repellendus iure, iste.")

class Work_Experience(models.Model):
    Title = models.CharField(max_length=50,default="frontend developer / facebook")
    Started_at = models.DateField()
    Leave_at = models.DateField()
    Description = models.TextField(default="Lorem ipsum dolor sit amet. Praesentium magnam consectetur vel in deserunt aspernatur est reprehenderit sunt hic. Nulla tempora soluta ea et odio, unde doloremque repellendus iure, iste.")
class Education(models.Model):
        Title = models.CharField(max_length=50,default="frontend developer / facebook")
        Started_at = models.DateField()
        Leave_at = models.DateField()
        Description = models.TextField(default="Lorem ipsum dolor sit amet.")
class Social_Links(models.Model):
    Facebook = models.URLField()
    Twitter = models.URLField()
    Pintrest = models.URLField()
    Instagram = models.URLField()
    Linkedin = models.URLField()
    
class contact (models.Model):
    Name = models.CharField(max_length=50) 
    Email = models.EmailField()
    Subject = models.CharField(max_length=200)
    Message = models.TextField()
    
    def __str__(self):
        return self.Name

