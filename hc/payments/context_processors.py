from django.conf import settings
from django.http import HttpRequest

def payment_context(request: HttpRequest) -> dict:
    # Context processor to inject payment-related settings into templates
    return {"display_pricing": settings.USE_PAYMENTS}

