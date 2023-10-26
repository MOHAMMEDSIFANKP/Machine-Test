from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=250, unique=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class ShortTermCourse (models.Model):
    STATUS_CHOICES = (
        ('enable', 'enable'),
        ('disable', 'disable'),
    )
    image =  models.ImageField(upload_to='ShortTermCourse_image', null=True, blank=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    amount = models.BigIntegerField()
    description = models.TextField()
    status = models.CharField(max_length=30, default='enable', choices=STATUS_CHOICES)

