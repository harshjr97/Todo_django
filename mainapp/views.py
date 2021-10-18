from django.shortcuts import render, redirect
from .models import ToDo

# Create your views here.

def home(request):
    if request.method=="POST":
        title = request.POST['title']
        if title !='':
            ToDo.objects.create(title=title)
        return redirect('home')
    data = ToDo.objects.all().order_by('created_at')
    context = {'data':data}
    return render(request, 'index.html', context)


def delete(request, id):
    ToDo.objects.get(id=id).delete()
    return redirect('home')


def done(request, id):
    data = ToDo.objects.get(id=id)
    data.complete = True
    data.save()
    return redirect('home')

def undone(request, id):
    data = ToDo.objects.get(id=id)
    data.complete = False
    data.save()
    return redirect('home')