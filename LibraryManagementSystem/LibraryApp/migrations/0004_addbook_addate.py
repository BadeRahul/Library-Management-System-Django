# Generated by Django 3.0 on 2023-09-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0003_addbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbook',
            name='addate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
