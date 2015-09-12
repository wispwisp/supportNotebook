from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from .models import ResponseTemplate
from taggit.models import Tag

from urllib.parse import parse_qs


def index(request):
    return HttpResponseRedirect(reverse('responseTemplates:templates'))


def templates(request):
    templates = None
    if 'tag' in parse_qs(request.GET.urlencode()):
        tags = parse_qs(request.GET.urlencode())['tag']
        templates = ResponseTemplate.objects.all()
        for tag in tags:
            templates = templates.filter(tags__name__exact=tag)

    return render(request, 'responseTemplates/template.html', {
        'tags':Tag.objects.order_by('name'),
        'button_value':"Выберите теги",
        'templates':templates,
    })
