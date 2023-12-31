from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Logo(models.Model):
    image = models.ImageField(upload_to="images/logo")
    alt = models.CharField(max_length=50)

    def __str__(self):
        return self.alt


class About(models.Model):
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/services")
    alt = models.CharField(max_length=50)

    def __str__(self):
        return self.alt


class Service(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    icon = models.CharField(max_length=30, null=True, blank=True)

    # alt = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Facts(models.Model):
    lines = models.PositiveIntegerField()
    files = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    clients = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Fact'
        verbose_name_plural = 'Facts'

    def __str__(self):
        return 'HI'


class Portfolio(models.Model):
    CHOICES = (
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('development', 'Development'),
    )
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/portfolio")
    alt = models.CharField(max_length=50)
    sort = models.CharField(max_length=300, choices=CHOICES, default="design")

    def __str__(self):
        return self.title


class HomePageTags(models.Model):
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    locale = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:locale')
    type = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:type')
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:title')
    descriptionOg = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:description')
    site_name = models.CharField(max_length=400, blank=True, null=True, verbose_name='Og:site_name')
    modified_time = models.CharField(max_length=500, blank=True, null=True, verbose_name='Modified_time')

    class Meta:
        verbose_name = 'HomePage Tag'
        verbose_name_plural = 'HomePage Tags'

    def __str__(self):
        return "HomePage Tags"
