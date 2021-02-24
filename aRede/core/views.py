from django.shortcuts import render, redirect
from django.http import response
 

# Create your views here.
def inicial(request):   
    return render(request, 'inicial.html')