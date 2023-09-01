from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    body = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to="images/articles")
    alt = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.datetime.now())

    # tags
    description = models.CharField(max_length=500, blank=True, null=True)
    canonical = models.CharField(max_length=500, blank=True, null=True)
    localeOg = models.CharField(max_length=500, blank=True, null=True)
    typeOg = models.CharField(max_length=500, blank=True, null=True)
    titleOg = models.CharField(max_length=500, blank=True, null=True)
    descriptionOg = models.CharField(max_length=500, blank=True, null=True)
    site_name = models.CharField(max_length=500, blank=True, null=True)
    widthOg = models.PositiveIntegerField(blank=True, null=True)
    heightOg = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]


class Message(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username} = {self.article.title}"

    class Meta:
        ordering = ('-created_at',)


class Tags(models.Model):
    pagetitle = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    locale = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    descriptionOg = models.CharField(max_length=500, blank=True, null=True)
    site_name = models.CharField(max_length=500, blank=True, null=True)
    modified_time = models.CharField(max_length=500, blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Blog Page Tag'
        verbose_name_plural = 'Blog Page Tags'

    def __str__(self):
        return "Blog Page Tags"
