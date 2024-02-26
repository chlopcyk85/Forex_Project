# forex_pr/urls.py
from django.urls import path
from forex_app.views import forex_view

urlpatterns = [
    path('', forex_view, name='forex'),

]
