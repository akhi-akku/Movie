from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import Movies


# Create your views here.
def index(request):
    movie=Movies.objects.all()

    return render(request,"index.html",{'movie_list':movie})

def detail(request,movie_id):
    movie=Movies.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie_det':movie})

def add_movie(request):
    if request.method=='POST':
        mname=request.POST['name']
        mdesc = request.POST['desc']
        myear = request.POST['year']
        mimg = request.FILES['img']
        movie=Movies(name=mname,desc=mdesc,year=myear,img=mimg)
        movie.save()
        return redirect('/')
    return render(request,"add.html")

def update(request,movie_id):
    movie=Movies.objects.get(id=movie_id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'m_movie':movie,'m_form':form})


def delete(request,movie_id):
        if request.method=='POST':
            movie=Movies.objects.get(id=movie_id)
            movie.delete()
            return redirect('/')
        return render(request,"delete.html")