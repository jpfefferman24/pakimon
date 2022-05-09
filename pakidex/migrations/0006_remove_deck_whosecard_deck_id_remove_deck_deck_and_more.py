# Generated by Django 4.0.3 on 2022-05-05 17:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pakidex', '0005_alter_card_species_alter_card_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='whoseCard',
        ),
        migrations.AddField(
            model_name='deck',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='deck',
            name='deck',
        ),
        migrations.AddField(
            model_name='deck',
            name='deck',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
