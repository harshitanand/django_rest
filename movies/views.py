from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from movies.serializers import UserSerializer, MoviesSerializer
from movies.models import MoviesList
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = MoviesList.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.AllowAny)

def search(request):
    return render(request, 'search.html')

def result(request):
    context_dict = {}
    if request.method == 'POST':
        data = request.POST['search']
        movies = MoviesList.objects.filter(name = data)
        context_dict['movies'] = movies
        return render(request, 'result.html', context_dict)
