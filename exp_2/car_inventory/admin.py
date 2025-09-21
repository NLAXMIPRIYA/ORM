from django.contrib import admin
from .models import CarInventory
class CarInventoryAdmin(admin.ModelAdmin):
    list_display=["car_name"]
    fieldsets = (
        ("Car Details", {
            "fields": ("car_name", "plate_number", "car_color")
        }),
        ("Purchase & Specs", {
            "fields": ("purchase_date", "mileage")
        }),
    )
    list_display=["car_name","plate_number","car_color","purchase_date","mileage"]
    date_hierarchy="purchase_date"
    actions_selection_counter=True
admin.site.register(CarInventory,CarInventoryAdmin)

