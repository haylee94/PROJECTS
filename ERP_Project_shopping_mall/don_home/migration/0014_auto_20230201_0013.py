# Generated by Django 3.2.3 on 2023-01-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('don_home', '0013_naverproductinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naverproductinfo',
            name='productModificationDate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='naverproductinfo',
            name='productRegistrationDate',
            field=models.CharField(max_length=100),
        ),
    ]