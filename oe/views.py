from django.http import HttpResponse
from django.shortcuts import render

'''网站主页'''

def index(request):
    return render(request, 'oe/homepage.html')

'''六西格玛的内容'''
def sixsigmaoverview(request):
    return render(request, 'oe/sixsigma/overview.html')

def sixsigmadefine(request):
    return render(request, 'oe/sixsigma/define.html')

def sixsigmavoc(request):
    return render(request, 'oe/sixsigma/voc.html')

def sixsigmaid(request):
    return render(request, 'oe/sixsigma/id.html')

def sixsigmacustomerdatacollection(request):
    return render(request, 'oe/sixsigma/customerdatacollection.html')

'''精益生产的内容'''
def lean(request):
    return HttpResponse("<h1>敬请期待！</h1>")
##    return render(request, 'oe/lean/leanoverview.html')

'''供应链的内容'''
def supplychain(request):
    return HttpResponse("<h1>敬请期待！</h1>")
