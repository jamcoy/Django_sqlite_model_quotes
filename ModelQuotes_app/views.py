from django.shortcuts import render
from ModelQuotes_app.models import Quote


def get_quotes(request):
    return render(request, "ModelQuotes/home.html",
                  {'quote_list': Quote.objects.all()})

