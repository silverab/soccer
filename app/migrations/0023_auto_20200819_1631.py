# Generated by Django 2.2.7 on 2020-08-19 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20200819_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countryblog',
            options={'ordering': ['-date']},
        ),
        migrations.AlterUniqueTogether(
            name='countryblog',
            unique_together={('title', 'slug')},
        ),
    ]