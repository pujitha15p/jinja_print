from india.views import *

from django.urls import path

app_name='anything'

urlpatterns=[
    path('kohli/',kohli,name='kohli'),
    path('puji/',puji,name='puji'),
    
]