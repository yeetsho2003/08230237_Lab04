from django.contrib import admin
from .models import LearningJourney, AboutMe
# Register your models here.
# Register models to appear in admin interface
admin.site.register(LearningJourney)
admin.site.register(AboutMe)