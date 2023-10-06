from  django.db import models



class WeEat(models.Model):
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    title=models.CharField(max_length=500)
    price=models.IntegerField()
    body=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return self.title
class Signup(models.Model):
    fullname= models.CharField(max_length=500)
    email=models.EmailField(max_length=30)
    username = models.CharField(max_length=100)
    password=models.IntegerField()

    
    