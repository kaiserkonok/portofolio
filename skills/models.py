from django.db import models



# Skill model

class Skill(models.Model):
    skill_name = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(choices=[
        ('beginner', 'Beginner'),
        ('intermadiate', 'Intermadiate'),
        ('expert', 'Expert')
    ], max_length=20)
    thumbnail = models.ImageField()
