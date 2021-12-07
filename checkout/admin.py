from django.contrib import admin
from .models import OrderItem, OtherLineItem

# Register your models here.


class OtherLineItemAdminInline(admin.TabularInline):
    model = OtherLineItem
    readonly_fields = ('lineitem_total',)


class OrderItemAdmin(admin.ModelAdmin):
    inlines = (OtherLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(OrderItem, OrderItemAdmin)
