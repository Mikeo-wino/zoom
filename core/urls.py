from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('privacy.html/', privacy, name='privacy'),
    path('terms.html/', terms, name='terms'),
    path('article.html/', article, name='article'),
    path('contact.html/', content_request, name='contact'),
]
