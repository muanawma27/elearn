# Generated by Django 3.2.2 on 2021-05-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]