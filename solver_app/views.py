from django.shortcuts import render
import solver_app.word_lib as word_lib

# Create your views here.

globalDict = word_lib.getDict()

def home(request):
    context = dict()

    if request.method == 'POST':
        # Somebody did inspect element on the frontend to mess up the form
        if 'word' not in request.POST:
            context['error'] = 'Nice try! Please actually submit a word :)'
        else:
            ogWord = request.POST.get('word')
            context['og_word'] = ogWord
            context['steals'] = word_lib.getPossibleSteals(globalDict, ogWord)

    # If method is GET, context is empty, so home.html will populate with a form
    return render(request, 'solver_app/home.html', context)
