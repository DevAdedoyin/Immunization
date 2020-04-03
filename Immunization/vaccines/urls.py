from django.conf.urls import url
from .views import chars

urlpatterns = [
                url(r'^/vaccine/(?P<vaccine>[\w\-]+)/', chars, name='vaccine'),
]