#forms.py
from django import forms


class ForexForm(forms.Form):
    currency_pair = forms.ChoiceField(choices=[('USDJPY', 'USD/JPY'), ('USDEUR', 'USD/EUR'),
                                               ('EURGBP', 'EUR/GBP'), ('EURAUD', 'EUR/AUD'),
                                               ('EURNZD', 'EUR/NZD'), ('EURCAD', 'EUR/CAD'),
                                               ('EURCHF', 'EUR/CHF'), ('GBPUSD', 'GBP/USD'),
                                               ('AUDUSD', 'AUD/USD'), ('EURPLN', 'EUR/PLN'),
                                               ('CHFPLN', 'CHF/PLN'), ('BTCUSD', 'BTC/USD')],
                                     widget=forms.RadioSelect, required=True)
