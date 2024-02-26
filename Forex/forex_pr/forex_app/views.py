# forex_app/views.py

from django.shortcuts import render
from .forms import ForexForm
from .models import ForexResult
from forex_app.ax import forex, adx, adx_trend


def forex_view(request):
    if request.method == 'POST':
        form = ForexForm(request.POST)
        if form.is_valid():
            currency_pair = form.cleaned_data['currency_pair']
            data = forex(currency_pair)
            adx_value = adx(data)
            description = adx_trend(adx_value)

            ForexResult.objects.create(currency_pair=currency_pair, description=description)

            return render(request, 'result.html', {'currency_pair': currency_pair, 'description': description})
    else:
        form = ForexForm()

    return render(request, 'forex_form.html', {'form': form})


