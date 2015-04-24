from django.db import models

GENERS_LIST = ['Adventure', 'Family', 'Fantasy', 'Musical', 'Sci-Fi', 'Drama', 'War', 'Horror', 'Mystery', 'Thriller', 'Romance', 'Crime', 'Western']
GENERS_CHOICE =sorted((item, item) for item in GENERS_LIST)

class MoviesList(models.Model):
    popularity = models.FloatField(default='0.0', blank=True)
    director = models.TextField(max_length=100, blank=True, default=' ')
    genere = models.CharField(choices=GENERS_CHOICE, max_length=100, default='Drama')
    imdb_score = models.FloatField(default='0.5', blank=False)
    name = models.CharField(unique=True, max_length=150, blank=False)

    def __str__(self):
        return self.name