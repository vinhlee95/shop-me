# Generated by Django 3.1.7 on 2021-03-21 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop', '0002_auto_20210317_0424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'permissions': [('can_view_shop_list', 'Can view shop list')]},
        ),
    ]
