#adx_app.py

import requests


def forex(symbol):
    url = f'https://www.alphavantage.co/query?function=ADX&symbol={symbol}&interval=daily&time_period=10&apikey=CAPMGGOOFLTTB9H2'
    r = requests.get(url)
    data = r.json()
    return data


def adx(data):
    adx_data = data.get('Technical Analysis: ADX')
    try:
        first_date = list(adx_data.keys())[0]
    except 'NoneType' :
        print("Nie pobrano danych z serwera, spróbuj ponownie później.")
    adx_value = adx_data[first_date]['ADX']
    print(f"Wartość wskaźnika ADX na godzinę: {first_date} wynosi: {adx_value}")
    return adx_value


def adx_trend(adx_value):
    if adx_value is not None:
        adx_value = float(adx_value)
        if adx_value < 20:
            return ("Wskazuje na słaby trend, co może sugerować, że rynek porusza się bokiem lub konsoliduje."
                    " Inwestorzy mogą rozważyć unikanie strategii związanych z trendem.")

        elif 20 < adx_value < 40:
            return ("Wskazuje na rozwijający się trend o umiarkowanej sile. "
                    "Inwestorzy mogą rozważyć strategie związane z trendem.")
        else:
            return ("Wskazuje na silny trend. Inwestorzy mogą rozważyć wejście lub "
                    "utrzymanie pozycji zgodnie z kierunkiem trendu.")
    else:
        return "Brak danych ADX."


if __name__ == '__main__':
    data = forex()
    adx_value = adx(data)
    description = adx_trend(adx_value)
    print(description)
