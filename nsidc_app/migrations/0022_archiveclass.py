# Generated by Django 4.0.6 on 2022-07-27 10:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nsidc_app', '0021_alter_myclass_slno'),
    ]

    operations = [
        migrations.CreateModel(
            name='archiveclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.CharField(max_length=2)),
                ('tenderno', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('releasedate', models.DateTimeField(default=django.utils.timezone.now)),
                ('closingdate', models.DateField()),
            ],
        ),
    ]