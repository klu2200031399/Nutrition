# Generated by Django 5.0.2 on 2024-04-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]