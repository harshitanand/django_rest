from rest_framework import serializers
from django.contrib.auth.models import User
from models import MoviesList

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = User
        fields = ('url', 'username', 'email', 'password', 'is_staff', 'is_active', 'is_superuser')

class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MoviesList
        fields = ('popularity', 'director', 'genere', 'imdb_score', 'name')