from django.shortcuts import render
import solver_app.word_lib as word_lib

# Create your views here.

globalDict = word_lib.getDict()

def home(request):
    context = dict()

    # Requesting a steal
    if request.method == 'POST':
        # Default both to None
        word = request.POST.get('word', None)
        letters = request.POST.get('letters', None)
        if letters == '':
            letters = None

        if word is None:
            context['error'] = 'Please submit a word!'

        # Word was provided
        else:
            context['steals'] = word_lib.getPossibleSteals(globalDict, word, letters)
            context['og_word'] = word
            if letters is not None:
                context['letters'] = letters

    # If method is GET, context is empty, so home.html will populate with a form
    return render(request, 'solver_app/home.html', context)
