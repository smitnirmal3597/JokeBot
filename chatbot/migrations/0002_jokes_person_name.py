# Generated by Django 3.1.4 on 2020-12-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokes',
            name='person_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
