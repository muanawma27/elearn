# Generated by Django 3.2.2 on 2021-05-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_rename_coveriamge_post_coverimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='coverimage',
            field=models.ImageField(null=True, upload_to='coverimage/'),
        ),
    ]
