from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
#    template = loader.get_template('risalec_smrecic/templates/index.html')
    return HttpResponse(render(request,'risalec_smrecic/index.html'))