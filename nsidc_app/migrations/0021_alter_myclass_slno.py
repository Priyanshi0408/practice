# Generated by Django 4.0.6 on 2022-07-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsidc_app', '0020_alter_myclass_closingdate_alter_myclass_releasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclass',
            name='slno',
            field=models.CharField(max_length=2),
        ),
    ]
