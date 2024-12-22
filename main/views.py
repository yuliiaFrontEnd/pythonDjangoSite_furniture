from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'The main page of the Home',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_autenticated': False
    }

    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    return HttpResponse('About page')
