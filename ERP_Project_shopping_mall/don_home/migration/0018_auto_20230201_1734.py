# Generated by Django 3.2.3 on 2023-02-01 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('don_home', '0017_cafe24cateory_cafe24coupon_cafe24oprder_cafe24product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cafe24Cateory',
            new_name='Cafe24Category',
        ),
        migrations.RenameModel(
            old_name='Cafe24Oprder',
            new_name='Cafe24Order',
        ),
    ]