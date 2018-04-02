import googlemaps
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def distance_matrix(request):
    key = 'AIzaSyDQuf9pefTf9pQ9WPVDV0ZS3qorE-XfiRU'
    if request.method == 'POST':
        client = googlemaps.Client(key)
        origins = request.POST['origins']
        destinations = request.POST['destinations']
        matrix = client.distance_matrix(origins, destinations)
        distance = matrix['rows'][0]['elements'][0]['distance']['text']
        print(distance)
        return render(request, 'index.html',{'distance':distance})
    else:
        return render(request, 'index.html')
