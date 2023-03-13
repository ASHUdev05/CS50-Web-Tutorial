from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "birthday/index.html", {
        "birthday": (datetime.datetime(now.year, 6, 13) - now)
    })