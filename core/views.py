from django.shortcuts import render
from django.utils.translation import ugettext
from django.http import HttpResponse


def index(request):
    output = ugettext("Текст из вьюхи, который нужно перевести")
    return render(request, 'core/index.html', {'output': output})
