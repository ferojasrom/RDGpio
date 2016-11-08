from django.shortcuts import render
import time
import RPi.GPIO as GPIO

# Create your views here.

def gpio_list(request):
    return render(request, 'RDGpio/gpio_list.html',{})
