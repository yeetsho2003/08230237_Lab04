from django.db import models

# Create your models here.
# Model to store learning journey info
class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# Model to store personal info
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # for screenshot/profile

    def __str__(self):
        return self.name