# Generated by Django 5.0.2 on 2024-02-15 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_Auth', '0006_remove_user_bio_remove_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
