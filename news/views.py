# views.py
from django.shortcuts import render, redirect
import requests


def myhome(request):
    return render(request,'myhome.html')
def select_country(request):
    return render(request, 'select_country.html')


def view_news(request):
    selected_country = request.GET.get('selected_country', 'us')  # Default to 'us' if no country selected
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': selected_country,
        'apiKey': '1b18bdba53fe479cabd3687b735a97c6'
    }

    response = requests.get(url, params=params , verify=False)
    news_data = response.json()
    articles = news_data['articles']


    return render(request, 'news.html', {'selected_country': selected_country, 'articles': articles})
