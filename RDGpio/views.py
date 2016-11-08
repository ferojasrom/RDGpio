from django.shortcuts import render
import time
import RPi.GPIO as GPIO
from .models import GPIOs

# Create your views here.

def gpio_list(request):
    gpios = GPIOs.objects.all().order_by('pin')
    return render(request, 'RDGpio/gpio_list.html',{'gpios': gpios})
