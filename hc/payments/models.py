from django.db import models
from django.contrib.auth import get_user_model

# Get the user model to ensure compatibility with custom user models
User = get_user_model()

class PaymentSubscription(models.Model):
    # Linking the subscription to the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Subscription details
    customer_reference = models.CharField(max_length=36, blank=True)
    payment_token = models.CharField(max_length=35, blank=True)
    subscription_reference = models.CharField(max_length=10, blank=True)
    plan_reference = models.CharField(max_length=10, blank=True)
    plan_description = models.CharField(max_length=50, blank=True)
    address_reference = models.CharField(max_length=2, blank=True)

    # Billing preferences
    is_invoice_enabled = models.BooleanField(default=True)
    billing_email = models.EmailField(blank=True)

    # Dates
    billing_date_next = models.DateField(null=True, blank=True)
    notification_date_renewal = models.DateField(null=True, blank=True)
    date_setup = models.DateField(null=True, blank=True)

    def terminate(self) -> None:
        # Placeholder for subscription termination logic
        pass

