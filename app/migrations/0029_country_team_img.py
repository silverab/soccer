# Generated by Django 2.2.7 on 2020-08-20 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_remove_country_feature_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='team_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
