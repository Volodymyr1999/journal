# Generated by Django 2.1.7 on 2019-04-06 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafedra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_cafedra', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_faculty', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.PositiveSmallIntegerField()),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_predmet', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentsGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_group', models.CharField(max_length=7)),
                ('cafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.Cafedra')),
                ('rozklad', models.ManyToManyField(to='journalapp.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.Cafedra')),
                ('lessons', models.ManyToManyField(to='journalapp.Lesson')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.StudentsGroup'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mark',
            name='predmet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='journalapp.Predmet'),
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.Student'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='predmet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.Predmet'),
        ),
        migrations.AddField(
            model_name='journal',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='journalapp.StudentsGroup'),
        ),
        migrations.AddField(
            model_name='cafedra',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.Faculty'),
        ),
    ]
