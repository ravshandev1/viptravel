from django.db import models
from .utils import generate_unique_filename


class Tour(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=generate_unique_filename)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Advantage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=generate_unique_filename)
    text = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to=generate_unique_filename)
    text = models.TextField()
    clients = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class Award(models.Model):
    image = models.ImageField(upload_to=generate_unique_filename)

    def __str__(self):
        return self.image.name


class Contact(models.Model):
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.phone
