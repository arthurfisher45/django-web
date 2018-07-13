from django.shortcuts import render
from django.utils import timezone
from .models import Instrument

def instrument_sum(request):
    #instruments = Instrument.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    instruments = Instrument.objects.all()
    return render(request, 'app/instrument_sum.html', {'instruments': instruments})
