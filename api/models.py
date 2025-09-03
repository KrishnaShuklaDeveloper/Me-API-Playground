from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    education = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    links = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(default=3)

    def __str__(self):
        return self.name

class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    links = models.JSONField(default=dict, blank=True)
    skills = models.ManyToManyField(Skill, related_name="projects", blank=True)

    def __str__(self):
        return self.title
