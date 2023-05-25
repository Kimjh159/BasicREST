from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


#  ListAPIView
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#  RetrieveAPIView
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


from django.shortcuts import render
import json
import os
from django.http import HttpResponse
from os import path

file1 = "BasicREST/testingData/"


def jsonview(request):
    file_path = os.getcwd() + "\\" + path.relpath(file1)
    # print("path :", os.getcwd())
    # print("json ", file_path)
    data = dict()

    with open(file_path + '\\BookData.json', 'r') as file_handler:
        data = json.load(file_handler)

    return HttpResponse(json.dumps(data), content_type='application/json')

import feedparser

def viewfeed(request):
    feeds = feedparser.parse('http://johnsmallman.wordpress.com/author/johnsmallman/feed/')
    #feeds = feedparser.parse('http://www.espn.com/espn/rss/news')
    return render(request, "viewFeed.html", {'feeds' : feeds})

def viewjson(request):
    return render(request, 'viewJSON.html')

def viewrest(request):
    return render(request, 'viewREST.html')

from django.shortcuts import render

def viewbar(request):
    return render(request, 'chart/viewbar.html')

def viewbubble(request):
    return render(request, 'chart/viewbubble.html')
def viewpie(request):
    return render(request, 'chart/viewpie.html')
def viewdynamic(request):
    return render(request, 'chart/viewdynamic.html')
def viewmultiple(request):
    return render(request, 'chart/viewmultiple.html')
def viewmap(request):
    return render(request, 'chart/viewmap.html')
