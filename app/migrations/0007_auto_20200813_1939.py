# Generated by Django 2.2.7 on 2020-08-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200813_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateField(),
        ),
    ]
