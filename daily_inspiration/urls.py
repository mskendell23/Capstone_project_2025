from django.urls import path
from . import views

# url for app - daily_inspiration and daily quote
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("api/random-quote/", views.random_quote, name="random_quote"),
    path("api/daily-quote/", views.daily_quote, name="daily_quote"),
]