from django.shortcuts import render
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

import services
from .models import Company
from .models import City

# Create your views here.

def index(request):
    companies = Company.objects.all()
    context = {'companies': companies, 'companies_json': serializers.serialize("json", Company.objects.all()), 'cities_json': serializers.serialize("json", City.objects.all())}
    
    return render(request, 'comdir/index.html', context)
