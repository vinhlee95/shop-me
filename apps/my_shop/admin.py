from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin

from .models import Shop


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ("name", "location", "address", "city")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        user_permissions = list(request.user.get_user_permissions())

        print(form.fields)
        # Specific permission to change name
        name_field = form.base_fields.get("name")
        if not name_field:
            print("No name field")
            return form

        if "my_shop.can_edit_shop_name" not in user_permissions:
            name_field.label = "Name (disabled)"
            name_field.disabled = True
        else:
            name_field.label = "Name (enabled)"

        return form
