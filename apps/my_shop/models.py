from django.contrib.gis.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    class Meta:
        permissions = [
            ("can_view_shop_list", "Can view shop list"),
            ("can_edit_shop_name", "Can edit shop name")
        ]
