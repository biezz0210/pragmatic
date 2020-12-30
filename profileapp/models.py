from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    # on_delete: 연결되있는 객체가 삭제될때 어떻게 될것인가? CASCADE : 함께 사라짐
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
