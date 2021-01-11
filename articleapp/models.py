from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project
# from uuid import uuid4


# def get_file_path(instance, filename):
#     uuid_name = uuid4().hex
#     return '/'.join(['article/', uuid_name])


# Create your models here.


class Article(models.Model):
    writer = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='article', null=True)

    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    # image = models.ImageField(upload_to=get_file_path, null=False)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_created=True, null=True)
