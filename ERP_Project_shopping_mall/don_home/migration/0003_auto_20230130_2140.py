# Generated by Django 3.2.3 on 2023-01-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('don_home', '0002_ably_token_cafe24'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe24',
            name='cafe24_client_secret',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='cafe24',
            name='cafe24_clientid',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='cafe24',
            name='cafe24_encode_csrf_token',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cafe24',
            name='cafe24_mallid',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='cafe24',
            name='cafe24_redirect_uri',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='cafe24',
            name='cafe24_id',
            field=models.CharField(max_length=200, verbose_name='아이디'),
        ),
        migrations.AlterField(
            model_name='cafe24',
            name='cafe24_pw',
            field=models.CharField(max_length=200, verbose_name='비밀번호'),
        ),
    ]
