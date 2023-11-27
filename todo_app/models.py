from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    email = models.EmailField(max_length=120, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']




class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    complete = models.BooleanField()
    create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
    

