from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    contact = models.CharField(max_length=10,null=True)
    branch = models.CharField(max_length=50)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
    

class UploadedNotes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.DateField(auto_now_add=True)
    branch = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    notesfile = models.FileField()
    filetype = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20)


    def __str__(self):
        return self.user.username+" "+ self.status
    
class Help(models.Model):
    uploadingdate = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
 