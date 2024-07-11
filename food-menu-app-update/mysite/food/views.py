from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Item
from .form import ItemForm
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    items = Item.objects.all()
    context = {
        'items':items
    } 
    return HttpResponse(template.render(context,request))

def detail(request,item_id):

    item = Item.objects.get(pk=item_id)
    context = {'item':item}
    return render(request,'detail.html',context=context)
def addItem(request):
    # if this is a POST request we need to process the form data
    form = ItemForm(request.POST)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect('food:index')

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "add.html", {"form": form})

def editItem(request,item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None,instance=item)

    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect('food:index')
    else:
        return render(request,"add.html",{"form":form,"item":item})
    
def delete(request,item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('food:index')
