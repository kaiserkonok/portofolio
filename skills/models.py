from django.db import models
from PIL import Image


# Skill model

class Skill(models.Model):
    skill_name = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(choices=[
        ('beginner', 'Beginner'),
        ('intermadiate', 'Intermadiate'),
        ('expert', 'Expert')
    ], max_length=20)
    thumbnail = models.ImageField(upload_to='skills/')

    def clean_thumbnail(self):
        img = Image.open(self.thumbnail)
        if img.height < 300 or img.width < 300:
            raise ValidationError("Image must be at least 300x300 pixels")

    def __str__(self):
        return self.skill_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.thumbnail.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)
