# Generated by Django 3.2.2 on 2021-06-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210603_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='userikigai',
            name='interest_ikigai2_value',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
