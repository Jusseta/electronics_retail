from django.contrib import admin
from chain.models import RetailChain, Contacts, Product


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'country', 'city', 'street', 'building']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date']


@admin.register(RetailChain)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ['name', 'contacts', 'provider', 'debt', 'created_at']
    list_display_links = ['name', 'provider']
    actions = ["reset_debt"]

    @admin.action(description="clears the debt to the supplier for selected objects")
    def reset_debt(self, request, queryset):
        queryset.update(debt=0.00)
