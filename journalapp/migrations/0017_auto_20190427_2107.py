# Generated by Django 2.1.7 on 2019-04-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0016_remove_subject_id'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='subject',
        #     name='id',
        #     field=models.IntegerField(default=13),
        # ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=200,primary_key=True,serialize=False),
        ),
    ]
