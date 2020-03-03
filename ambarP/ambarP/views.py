from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def index(request):
    template = loader.get_template('index.html')

    document  = template.render()

    return HttpResponse(document)