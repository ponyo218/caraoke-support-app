from django.shortcuts import render, get_object_or_404
from .models import Song, Singer
import json
from django.http import HttpResponse
import requests


def all_song(request):
    songs = Song.objects.order_by('title')
    print('all_song')
    return render(request, 'app/all_song.html', {'songs': songs})


def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'app/song_detail.html', {'song': song})


def render_json_response(request, data, status=None):
    #response を JSON で返却
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response


def iTunes_search(request):

    item_data = Singer.objects.all()

    lz = []
    data_list = []

    sss = 0
    maxNum = "5"

    for x in item_data:
        z = x.__str__()
        lz.append(z)
        keyWord = lz[sss]
        print(lz[sss])

        url = 'https://itunes.apple.com/search?lang=ja&entry=music&media=music&country=JP&limit='+ maxNum +'&term=' + keyWord

        headers = {"content-type": "application/json"}
        r = requests.get(url, headers=headers)
        data = r.json()
        data_list.append(data)
        print(data_list)

        sss += 1

    return render_json_response(request, data_list) #JSON