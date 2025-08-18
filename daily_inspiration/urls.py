from django.urls import path
from . import views

# url for app - daily_inspiration and daily quote
urlpatterns = [
    path("", views.daily_quote, name="daily_quote"),
    path("api/daily-quote/", views.daily_quote, name="daily_quote"),
]