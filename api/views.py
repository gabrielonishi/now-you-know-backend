from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import ArtistSerializer, UserTrySerializer
from .models import Artist, UserTry

# Create your views here.
def main(request):
    return HttpResponse('Hello World')

@api_view(['GET'])
def api_artist(request, artist_name):
    try:
        artist = Artist.objects.get(name=artist_name)
    except Artist.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        new_artist_data = request.data
        input_name = new_artist_data['name']
        artist_name = Artist.normalize_name(input_name)
        artist = Artist(name=artist_name)
        artist.save()

    serialized_artist = ArtistSerializer(artist)
    return Response(serialized_artist.data)

# @api_view(['GET', 'POST'])
# def api_artists_list(request):
#     try:
#         artists_list = Artist.objects.all()
#     except Artist.DoesNotExist:
#         raise Http404()
    
#     if request.method == 'POST':
#         new_artist_data = request.data
#         input_name = new_artist_data['name']
#         new_artist = Artist(name=Artist.normalize_name(input_name))
#         new_artist.save()
    
#     serialized_artists = ArtistSerializer(artists_list, many=True)
#     return Response(serialized_artists.data)

# @api_view(['GET','POST'])
# def api_user_tries_list(request):
#     try:
#         user_tries = UserTry.objects.all()
#     except UserTry.DoesNotExist:
#         raise Http404()
#     if request.method == 'POST':
#         new_try_data = request.data
#         input_name = new_try_data['artist']
#         score = new_try_data['score']
#         artist_name = Artist.normalize_name(input_name)
#         artist = Artist.objects.filter(name=artist_name)
#         if artist:
#             new_try = UserTry(score=score, artist=artist[0])
#             new_try.save()
#         else:
#             artist = Artist(name=artist_name)
#             artist.save()
#             new_try = UserTry(score=score, artist=artist)
#             new_try.save()

#     serialized_tries = UserTrySerializer(user_tries, many=True)
#     return Response(serialized_tries.data)

@api_view(['GET','POST'])
def api_artist_tries(request, artist_name):
    try:
        # Método get_or_create devolve uma tupla
        # Se encontrar um objeto, created = false
        artist, created = Artist.objects.get_or_create(name=artist_name)
        artist_tries = UserTry.objects.filter(artist=artist)

    except Artist.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_try_data = request.data
        score = new_try_data['score']
        new_try = UserTry(score=score, artist=artist)
        new_try.save()
        
        # Pegando a pontuação das tentativas para editar o artista
        tries_list = []
        for user_try in artist_tries:
            tries_list.append(user_try.score)
        new_avg = sum(tries_list)/len(tries_list)
        print(tries_list)
        print(new_avg)
        artist.setRating(new_avg)
        artist.save()

    serialized_tries = UserTrySerializer(artist_tries, many=True)
    return Response(serialized_tries.data)
