from django.db import models

# Create your models here.
class Contact(models.Model):
      name=models.CharField(max_length=200)
      email=models.EmailField()
      subject=models.TextField()
      
      def __str__(self):
          return self.name
    
class Signin(models.Model):
      name=models.CharField(max_length=200)
      email=models.EmailField()
      number=models.TextField()
      home=models.TextField()
      date=models.DateField()
      
      def __str__(self):
          return self.name
    
class Mador(models.Model):
      name=models.CharField(max_length=200)
      email=models.EmailField()
      file=models.FileField()
      message=models.TextField()
      
      def __str__(self):
          return self.name
      
