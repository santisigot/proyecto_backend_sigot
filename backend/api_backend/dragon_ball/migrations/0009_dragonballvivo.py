# Generated by Django 5.0.4 on 2024-06-19 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragon_ball', '0008_rename_personaje_dragonballsaga_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dragonballvivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('vivo', models.BooleanField(default=False)),
            ],
        ),
    ]