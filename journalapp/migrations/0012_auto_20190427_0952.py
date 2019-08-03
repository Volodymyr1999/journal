# Generated by Django 2.1.7 on 2019-04-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0011_auto_20190425_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('date', models.DateField()),
                ('rowindex', models.IntegerField()),
                ('colindex', models.IntegerField()),
                ('journals', models.ManyToManyField(to='journalapp.Journal')),
                ('students', models.ManyToManyField(to='journalapp.Student')),
            ],
        ),
        migrations.AlterField(
            model_name='day',
            name='name_of_day',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday')], max_length=15),
        ),
    ]