from django.shortcuts import render,redirect
from . forms import ImageUploadForm,ImageProfileForm,CommentForm
from .models import *
from django.contrib.auth.decorators import login_required
from vote.managers import  VotableManager
from django.contrib.auth.models import User
votes = VotableManager()

# Create your views here.
def home(request):

    return render(request,'insta/index.html')
