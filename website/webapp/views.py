from django.http import HttpResponse
from django.shortcuts import render
from .models import security
# Create your views here.
def demo(request):
    obj=security.objects.all()
    return render(request,"index.html",{'result':obj})