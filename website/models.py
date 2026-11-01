from django.db import models

# Create your models here.
class LandingPage(models.Model):

    logo = models.ImageField(verbose_name="Logo")
    name = models.CharField(max_length=50)
    overview = models.TextField()

    about_me = models.TextField()
    email = models.EmailField()
    github_link = models.URLField()
    linkedin_link = models.URLField()


class Project(models.Model):

    title = models.CharField(max_length=100)
    short_description = models.TextField()
    created_at = models.DateTimeField()

    