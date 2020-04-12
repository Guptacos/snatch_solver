from django.contrib.auth.models import User
# Django transaction system so we can use @transaction.atomic for registration
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from socialnetwork.forms import *
from socialnetwork.models import *
import socialnetwork.word_lib as word_lib

# Create your views here.

globalDict = word_lib.getDict()

def home(request, word=None):
    print(word)
    context = {'og_word': word}

    if word is None:
        context['og_word']= 'Please append /word to the url!'
    else:
        context['words'] = word_lib.getPossibleSteals(globalDict, word)

    return render(request, 'socialnetwork/home.html', context)
