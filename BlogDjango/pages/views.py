from django.shortcuts import render
from .models import Page
# Create your views here.
def getPage(request, slugURL):

    page = Page.objects.get(slug=slugURL)
    
    return render(request,'pages/page.html',
    {
        "page": page
    })