from django.contrib import admin
from chain.models import RetailChain, Contacts, Product


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'building',)
    list_filter = ('country', 'city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date',)


@admin.register(RetailChain)
class RetailChainAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'provider', 'debt',)
    list_filter = ('contacts__country', 'contacts__city',)
    list_display_links = ('name', 'provider',)
    actions = ('reset_debt',)

    @admin.action(description='Reset the debt')
    def reset_debt(self, request, queryset):
        queryset.update(debt=0.00)
