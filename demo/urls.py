from django.conf.urls import url, include
from rest_framework import routers
from movies import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MoviesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^search-movies/', views.search, name="search-movie"),
    url(r'^results/', views.result, name="result"),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]