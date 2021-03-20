import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.contrib.gis.db.models.functions import Distance

from .models import Shop


@login_required(login_url="/login")
def list_all_shops(request):
    context = {}
    try:
        home_location = Shop.objects.get(name='Home')
    except Shop.DoesNotExist:
        logging.error('Missing location with "Home" name in the DB')
        context['error'] = 'Missing location with "Home" name in the DB'
        return render(request, 'home.html', context)

    shops = Shop.objects.annotate(distance=Distance('location', home_location.location)).order_by('distance')[0:6]

    # Format the distance so that it does not have any decimals
    for shop in shops:
        shop.parse_distance = f'{int(shop.distance.m)} m'
        # Round decimals if we want to: f'{round(shop.distance.m, 0)}m'

    context['shops'] = shops

    return render(request, 'home.html', context)


def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("shop-list")
        else:
            # Render login form
            form = AuthenticationForm()
            return render(request, "login.html", {"form": form, "error": form.error_messages})

