from django.shortcuts import render
from .models import Blogpost as Post

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def blogpost(request):
     allpost=[]
     return render(request,'blog/blogpost.html')
