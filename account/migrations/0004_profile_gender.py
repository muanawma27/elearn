# Generated by Django 3.2.2 on 2021-05-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_profilephoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=200, null=True),
        ),
    ]