from django.contrib import admin

from .models import UserSubscription , SubscriptionPlan

# Register your models here.
@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'price', 'billing_cycle')
    search_fields = ('plan_name',)
    ordering = ('price',)
    
@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'status')
    search_fields = ('user__email', 'plan__plan_name')
    ordering = ('-start_date',)
    

