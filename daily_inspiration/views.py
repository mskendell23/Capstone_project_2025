from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  .models import Quote
from .serializers import QuoteSerializer
import random
import datetime


# Daily Quote request (HTML Page)
@login_required
def homepage(request):
    categories = ["Motivation", "Faith", "Love"]
    selected_category = random.choice(categories)

    quotes = Quote.objects.filter(category=selected_category)
    quote = random.choice(quotes) if quotes else None
    
    return render(request, "daily_quote.html", {"quote": quote, "category": selected_category})

# API endpoints: 
# Daily Quote: Returns the same quote for the current day
@api_view(['GET'])
def daily_quote(request):
    quotes = Quote.objects.all()
    if quotes.exists():
        # Use today's date to pick the same "daily quote"
        today = datetime.date.today()
        index = today.toordinal() % quotes.count()
        quote = quotes[index]
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)
    return Response({"message": "No quotes available"})

# Random Quote: Returns a completely random quote each time
@api_view(['GET'])
def random_quote(request):
    quotes = Quote.objects.all()
    if quotes.exists():
        quote = random.choice(quotes)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)
    return Response({"message": "No quotes available"})