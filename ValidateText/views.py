from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import Product
from math import ceil

def index(request):
    return render(request,'Home.html')

def about(request):
    products = Product.objects.all()
    p_count = len(products)
    n_slides = p_count//4 + ceil((p_count/4)-(p_count/4))
    params = {'no_of_slides':n_slides,'range':range(1,n_slides),'product':products}
    return render(request,'about.html',params)

def contactus(request):
    return render(request,'contactus.html')

@login_required(login_url="/acounts/login/")
def analyze(request):
    if request.method == 'GET':
        dj_text = request.GET.get('text', 'default')
        puntuation = '~!#$%@^&*()_+=|\/?,<.>[]{}'

        removepunc = request.GET.get('removepunc','off')
        uppercase = request.GET.get('uppercase','off')
        newlineremover = request.GET.get('newlineremover','off')
        extraspaceremover = request.GET.get('extraspaceremover','off')
        analyzed=''
        if removepunc == 'on':
            analyzed = ''
            for char in dj_text:
                if char not in puntuation:
                    analyzed+=char
            dj_text = analyzed

        if uppercase == 'on':
            analyzed = ''
            for char in dj_text:
                analyzed += char.upper()
            dj_text = analyzed

        if newlineremover == 'on':
            analyzed = ''
            for char in dj_text:
                if char != '\n' and char != '\r':
                    analyzed += char
            dj_text = analyzed

        if extraspaceremover == 'on':
            analyzed = ''
            for index, char in enumerate(dj_text):
                if dj_text[index] != int(len(dj_text)):
                    if not(dj_text[index] == ' ' and dj_text[index+1] == ' '):
                        analyzed += char

        if (removepunc != 'on' and uppercase != 'on' and newlineremover != 'on' and extraspaceremover != 'on'):
            context = {
                'Purose': 'No Text Found',
                'text': analyzed
            }
        else:
            context = {
                'Purose': 'Analyzed Text',
                'text': analyzed
            }
        return render(request,'analyze.html', context)


@login_required(login_url="/acounts/login")
def Analyze_Text(request):
    return render(request,'validateText.html')