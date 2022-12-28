from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

from .models import Cat,CatManager

def show_cat(request):
    template_name = 'cat/cat_list.html'
    context = {'cat_list': Cat.objects.all()}
    return render(request, template_name, context)
def show_map(request):
    return render(request, 'showmap.html')

def show_onecat(request):
    if request.method=='GET':
        cid=request.GET.get("id")
        cat=Cat.objects.get(cat_id=cid)
        context={"cat":cat}
        return render(request, 'show_onecat.html',context)

def show_catandfeeder(request):
    manager_list = CatManager.objects.all()
    return render(request, 'show_catandfeeder.html',
        {'manager_list': manager_list})
