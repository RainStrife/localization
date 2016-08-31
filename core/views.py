from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse


def index(request):
    output = _("Текст из вьюхи, который нужно перевести")
    return render(request, 'core/index.html', {'output': output})
