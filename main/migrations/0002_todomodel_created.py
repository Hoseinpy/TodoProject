# Generated by Django 5.0.3 on 2024-03-19 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
