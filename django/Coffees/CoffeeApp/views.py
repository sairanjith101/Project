from django.shortcuts import render
from CoffeeApp.models import Coffee

# Create your views here.

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'CoffeeApp/index.html', {'coffee': coffee})
