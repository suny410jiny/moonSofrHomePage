from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.shortcuts import resolve_url
# Create your models here.


class User(AbstractUser):

    pass