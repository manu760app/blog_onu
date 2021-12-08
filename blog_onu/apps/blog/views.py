from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
  

def signin_signup(request):

 return render(request, 'signin_signup.html')


