import logging
from django.shortcuts import render
from django.contrib.gis.db.models.functions import Distance

from .models import Shop


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
