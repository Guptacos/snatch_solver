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
from socialnetwork.word_lib import *

# Create your views here.

def home(request, word=None, letters=None):
    print(word, letters)
    context = {'og_word': word, 'letters': letters}

    if word is None:
        context['og_word']= 'Please append /word/letters to the url!'
    elif letters is None:
        context['words'] = list(getPossibleSteals(word))
    else:
        context['words'] = list(newWordsManyLetters(word, letters))

    print(word, letters)

    return render(request, 'socialnetwork/home.html', context)
