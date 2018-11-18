from django.shortcuts import render
from django.http import HttpResponse
# from ipywidgets import
from arcgis.gis import GIS

def home(request):
    gis = GIS()
    print("Logged in as " + str(gis.properties.user.username))
    map_sj = gis.map("San Jose, CA")
    map_js = 'require(["esri/views/MapView"], function(MapView) {' \
             ' });'
    return_view = '<h1>Home page</h1><br>'+str(map_sj)
    return HttpResponse(return_view)
    return render(request, 'deforest/home.html')


def about(request):
    return HttpResponse('<h1>About page</h1>')
