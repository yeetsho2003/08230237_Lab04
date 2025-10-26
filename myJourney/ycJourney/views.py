from django.shortcuts import render
from .models import LearningJourney, AboutMe
# Create your views here.
# Index page view
def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'index.html', {'journeys': journeys})

# About Me page view
def about_me(request):
    me = AboutMe.objects.first()  # assume only one entry
    return render(request, 'aboutMe.html', {'me': me})