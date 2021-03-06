# Generated by Django 4.0.3 on 2022-03-14 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pakiName', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('deck', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pakimon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pakiName', models.CharField(max_length=280)),
                ('paki', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pakidex.card')),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moveName', models.CharField(max_length=280)),
                ('moveNum', models.IntegerField(default=-1)),
                ('move', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pakidex.card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='whoseDeck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pakidex.deck'),
        ),
    ]
