from django.utils import translation
from django.conf import settings
from ipware import get_client_ip
import geoip2.database
from pathlib import Path

COUNTRY_LANGUAGE_MAPPING = {
    'RU': 'ru',  # Россия
    'UA': 'uk',  # Украина
    'TR': 'tr',  # Турция
    'KR': 'ko',  # Южная Корея
    'US': 'en',  # США
    'GB': 'en',  # Великобритания
}

COUNTRY_CURRENCY_MAPPING = {
    'RU': 'RUB',  # Россия
    'UA': 'UAH',  # Украина
    'TR': 'TRY',  # Турция
    'KR': 'KRW',  # Южная Корея
    'US': 'USD',  # США
    'GB': 'GBP',  # Великобритания
    'EU': 'EUR',  # Европейский союз
}

class GeoLocationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.reader = geoip2.database.Reader(
            Path(settings.BASE_DIR) / 'geoip' / 'GeoLite2-Country.mmdb'
        )

    def __call__(self, request):
        if not request.session.get('geo_location_set'):
            client_ip, is_routable = get_client_ip(request)
            
            try:
                if client_ip and is_routable:
                    response = self.reader.country(client_ip)
                    country_code = response.country.iso_code
                    
                    # Устанавливаем язык
                    language_code = COUNTRY_LANGUAGE_MAPPING.get(country_code, settings.LANGUAGE_CODE)
                    if language_code in [lang[0] for lang in settings.LANGUAGES]:
                        request.session['django_language'] = language_code
                        translation.activate(language_code)
                    
                    # Устанавливаем валюту
                    currency_code = COUNTRY_CURRENCY_MAPPING.get(country_code, settings.CURRENCY_DEFAULT)
                    if currency_code in settings.CURRENCIES:
                        request.session['currency'] = currency_code
                    
                    request.session['geo_location_set'] = True
            except:
                pass  # В случае ошибки используем значения по умолчанию
        
        response = self.get_response(request)
        return response

    def __del__(self):
        self.reader.close() 