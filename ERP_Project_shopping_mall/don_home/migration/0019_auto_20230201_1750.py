# Generated by Django 3.2.3 on 2023-02-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('don_home', '0018_auto_20230201_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe24category',
            name='category_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cafe24category',
            name='display_type',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cafe24category',
            name='large_catetgory',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cafe24category',
            name='mid_category',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cafe24category',
            name='small_category',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cafe24category',
            name='sub_category',
            field=models.TextField(),
        ),
    ]
