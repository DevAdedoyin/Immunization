from django.conf.urls import url
from .views import search
from .views import home

urlpatterns = [
                url(r'^$', home, name='home'),
                url(r'^result/', search, name='result')
]