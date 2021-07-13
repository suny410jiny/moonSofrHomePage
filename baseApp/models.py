from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
import re

from moonsoft.util import uuid_name_upload_to


class commonColModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract =True

class Post(commonColModel):
    #
    title = models.CharField(blank=True, max_length=200)
    class PostChoices(models.TextChoices):
        Product = "PD", "Product"
        Projects = "PJ", "Projects"
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='my_post_set', on_delete=models.CASCADE)
    tag = models.CharField(max_length=100, blank=True)
    postDivision = models.CharField(max_length=10,choices=PostChoices.choices)
    tag_set = models.ManyToManyField('Tag', blank=True)
    caption = models.CharField(max_length=500)
    thumnail = models.ImageField(upload_to=uuid_name_upload_to)
    body = RichTextUploadingField(blank=True, null=True)
    def __str__(self):
        return self.caption

    def extract_tag_list(self):
        tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.tag)
        tag_list = []
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list

    def get_absolute_url(self):
        return reverse("baseApp:product_detail", args=[self.pk])

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super().save_model(request, obj, form, change)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Comment(commonColModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    class Meta:
        ordering = ['-id']
