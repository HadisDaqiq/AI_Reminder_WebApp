# Generated by Django 2.2.dev20180906114925 on 2019-04-12 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remind', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='reminder_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='remind.Location'),
        ),
    ]
