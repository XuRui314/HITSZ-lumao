from . import views
from django.conf.urls import url
from django.urls import path

from .views import show_cat,show_map,show_onecat,show_catandfeeder


app_name = 'cat'
urlpatterns = [
    path('', show_cat, name='cat'),
    path('map/', show_map),
    path('onecat/', show_onecat),
    path('catandfeeder/', show_catandfeeder),

]
