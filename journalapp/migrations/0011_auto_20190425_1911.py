# Generated by Django 2.1.7 on 2019-04-25 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0010_auto_20190425_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='subjects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journalapp.Subject'),
        ),
    ]
