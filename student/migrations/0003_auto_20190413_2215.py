# Generated by Django 2.1.7 on 2019-04-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190404_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='father',
            field=models.IntegerField(blank=True, default=8140516739, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother',
            field=models.IntegerField(blank=True, default=7984426396, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='std_no',
            field=models.IntegerField(blank=True, default=8154057515, null=True),
        ),
    ]