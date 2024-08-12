import requests
from django.shortcuts import render

def weather_view(request):
    weather_data = None
    error_message = None

    if 'city' in request.GET:
        city = request.GET['city']
        api_key = '75ac5818fb4e46fe9ff100822240708'
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

        try:
            response = requests.get(url, timeout=10)  # Increased timeout
            response.raise_for_status()
            weather_data = response.json()
        except requests.exceptions.HTTPError as http_err:
            error_message = f"HTTP error occurred: {http_err}"
        except requests.exceptions.ConnectionError as conn_err:
            error_message = f"Connection error occurred: {conn_err}"
        except requests.exceptions.Timeout as timeout_err:
            error_message = f"Timeout error occurred: {timeout_err}"
        except requests.exceptions.RequestException as req_err:
            error_message = f"An error occurred: {req_err}"

    return render(request, 'weather/weather.html', {'weather_data': weather_data, 'error_message': error_message})
