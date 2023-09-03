from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to="images/articles", verbose_name='Image')
    alt = models.CharField(max_length=100, verbose_name='Alt')
    body = CKEditor5Field('Text', config_name='extends')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return self.title