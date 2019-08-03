# Generated by Django 2.1.7 on 2019-04-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['time']},
        ),
        migrations.RemoveField(
            model_name='studentsgroup',
            name='rozklad',
        ),
        migrations.AddField(
            model_name='lesson',
            name='day_name',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Monday', max_length=10),
        ),
        migrations.AddField(
            model_name='lesson',
            name='group',
            field=models.ManyToManyField(to='journalapp.StudentsGroup'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='room',
            field=models.CharField(default='111', max_length=5),
        ),
    ]
