# Generated by Django 5.0.4 on 2024-06-18 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dragon_ball', '0003_alter_dragonball_años'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dragonball',
            old_name='nombre',
            new_name='name',
        ),
    ]
