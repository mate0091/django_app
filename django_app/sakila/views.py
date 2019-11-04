from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import *

def act(request):

    if request.method == "POST":
        form = ActorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = ActorForm()

    return render(request, "index.html", {"form": form})

def show_actor(request):

    actors = Actor.objects.all()
    return render(request, "show.html", {"actors": actors})

def edit_actor(request, id):

    actor = Actor.objects.get(actor_id=id)
    return render(request, "edit.html", {"actor": actor})

def update_actor(request, id):

    actor = Actor.objects.get(actor_id=id)
    form = ActorForm(request.POST, instance=actor)

    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request, "edit.html", {"actor": actor})

def destroy_actor(request, id):

    actor = Actor.objects.get(actor_id=id)
    actor.delete()
    return redirect("/show")

def flm(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/film_show")
            except:
                pass
        else:
            print(form.errors)
    else:
        form = FilmForm()

    return render(request, "film_index.html", {"form": form})

def show_film(request):
    films = Film.objects.all()
    return render(request, "film_show.html", {"film": films})

def edit_film(request, id):

    film = Film.objects.get(film_id=id)
    return render(request, "film_edit.html", {"film": film})

def update_film(request, id):

    film = Film.objects.get(film_id=id)
    form = FilmForm(request.POST, instance=film)

    if form.is_valid():
        form.save()
        return redirect("/film_show")

    else:
        print(form.errors)

    return render(request, "film_edit.html", {"film": film})

def destroy_film(request, id):

    film = Film.objects.get(film_id=id)
    film.delete()
    return redirect("/film_show")

def flmac(request):
    if request.method == "POST":
        form = FilmActorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/filmactor_show")
            except:
                pass
        else:
            print(form.errors)
    else:
        form = FilmForm()

    return render(request, "filmactor_index.html", {"form": form})

def show_film(request):
    filmactors = FilmActor.objects.all()
    return render(request, "film_show.html", {"film": filmactors})

def edit_film(request, id1, id2):

    filmactor = FilmActor.objects.get(film_id=id)
    return render(request, "filmactor_edit.html", {"film": filmactor})

def update_film(request, id1, id2):

    film = Film.objects.get(film_id=id)
    form = FilmForm(request.POST, instance=film)

    if form.is_valid():
        form.save()
        return redirect("/film_show")

    else:
        print(form.errors)

    return render(request, "film_edit.html", {"film": film})