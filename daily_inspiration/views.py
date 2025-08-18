from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  .models import Quote
from .serializers import QuoteSerializer
import random


# Daily Quote request
def daily_quote(request):
    categories = ["motivation", "faith", "love"]
    selected_category = random.choice(categories)

    quotes = Quote.objects.filter(category=selected_category)
    quote = random.choice(quotes) if quotes else None
    
    return render(request, "daily_quote.html", {"quote": quote, "category": selected_category})

# New API endpoint
@api_view(['GET'])
def daily_quote(request):
    quotes = Quote.objects.all()
    if quotes.exists():
        quote = random.choice(quotes)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)
    return Response({"message": "No quotes available"})