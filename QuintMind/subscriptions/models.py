from django.db import models
from django.conf import settings

class SubscriptionPlan(models.Model):
    """
    Stores the different subscription plans available (e.g., Free, Premium).
    """
    plan_name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(max_length=20) # e.g., 'monthly', 'annual'
    features_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.plan_name} (${self.price}/{self.billing_cycle})"


class UserSubscription(models.Model):
    """
    Links a User to a SubscriptionPlan and tracks its status.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscription')
    
    # If a plan is deleted, we set it to NULL,
    # but keep the subscription record for history.
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, related_name='subscriptions')
    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20) # e.g., 'active', 'cancelled', 'expired'

    def __str__(self):
        return f"{self.user.email} - {self.plan.plan_name} ({self.status})"