from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def terms(request):
    return render( request, 'Terms & Conditions/terms.html' )

def privacy(request):
    return render(request, 'privacy policy/index.html' )
def contact(request):
    return render(request, 'Contact/contact_us.html')

def error(request):
    return render(request, 'Contact/error.html')

def help(request):
    return render(request, 'help.html')