# Generated by Django 2.1.7 on 2019-04-25 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0008_auto_20190425_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='subjects',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='journalapp.Subject'),
        ),
    ]
