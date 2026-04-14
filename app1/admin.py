from django.contrib import admin
from .models import FoodItem, Order, OrderItem, Customer, Hotel

# Basic registrations
admin.site.register(Customer)
admin.site.register(Hotel)
admin.site.register(FoodItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('get_hotel', 'food_item', 'quantity')
    fields = ('get_hotel', 'food_item', 'quantity')

    def get_hotel(self, obj):
        return obj.food_item.hotel.name if obj.food_item.hotel else "Unknown"
    
    get_hotel.short_description = 'Spot/Hotel'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_order_summary', 'total_price', 'created_at')
    inlines = [OrderItemInline]

    def display_order_summary(self, obj):
        """
        Creates a list like:
        - Chicken Chowmein [Kausik]
        - Egg Chowmein [Sinka]
        - Momo [Sinka]
        """
        items = obj.orderitem_set.all()
        summary = []
        for item in items:
            hotel_name = item.food_item.hotel.name
            summary.append(f"{item.food_item.name} [{hotel_name}]")
        
        return ", ".join(summary)

    display_order_summary.short_description = 'Items & Spots'