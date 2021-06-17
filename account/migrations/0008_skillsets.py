# Generated by Django 3.2.2 on 2021-06-05 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0007_userikigai_interest_ikigai2_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillSets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professsion', models.IntegerField(default=0)),
                ('hobbies', models.IntegerField(default=0)),
                ('interests', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]