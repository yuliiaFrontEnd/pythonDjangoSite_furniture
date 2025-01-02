from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request) -> HttpResponse:

    categories = Categories.objects.all()
    context: dict[str, str] = {
        'title': 'Home main',
        'content': "Магазин мебели HOME",
        'categories': categories
        
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home main',
        'content': "About us",
        'text_on_page': "Information about furnitures."
    }

    return render(request, 'main/about.html', context)