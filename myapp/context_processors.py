from django.conf import settings

def currency_context(request):
    """
    Context processor that provides currency information to all templates.
    Returns:
        dict: A dictionary containing:
            - CURRENCIES: All available currencies
            - current_currency: The currently selected currency
            - currency_symbol: The symbol for the current currency
    """
    current_currency = request.session.get('currency', settings.CURRENCY_DEFAULT)
    return {
        'CURRENCIES': settings.CURRENCIES,
        'current_currency': current_currency,
        'currency_symbol': settings.CURRENCIES[current_currency]['symbol']
    } 