from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return HttpResponse ("please visit /random_word")

def random_word(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    request.session["counter"] += 1 
    request.session['new_word'] = get_random_string(length =14)
    return render (request, "index.html")

def reset (request):
    request.session.flush()
    return redirect('/random_word')