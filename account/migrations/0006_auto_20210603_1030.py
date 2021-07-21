# Generated by Django 3.2.2 on 2021-06-03 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_ikigaicategory_ikigais_userikigai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userikigai',
            name='hobby_ikigai1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='H I 1 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='hobby_ikigai2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='H I 2 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='hobby_ikigai3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='H I 3 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='hobby_ikigai4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='H I 4 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='hobby_ikigai5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='H I 5 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='interest_ikigai1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='I I 1 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='interest_ikigai2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='I I 2 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='interest_ikigai3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='I I 3 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='interest_ikigai4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='I I 4 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='interest_ikigai5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='I I 5 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='professsion_ikigai1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P I 1 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='professsion_ikigai2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P I 2 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='professsion_ikigai3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P I 3 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='professsion_ikigai4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P I 4 +', to='account.ikigais'),
        ),
        migrations.AlterField(
            model_name='userikigai',
            name='professsion_ikigai5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P I 5 +', to='account.ikigais'),
        ),
    ]
