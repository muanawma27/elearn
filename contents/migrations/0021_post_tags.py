# Generated by Django 3.2.2 on 2021-05-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0020_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(max_length=500, null=True),
        ),
    ]