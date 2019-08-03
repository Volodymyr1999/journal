from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    student_code = models.CharField(max_length=8, unique=True)
    group = models.ForeignKey('StudentsGroup',on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)


class StudentsGroup(models.Model):
    name_of_group = models.CharField(max_length=7)


    cafedra = models.ForeignKey('Cafedra',on_delete=models.CASCADE)


    def __str__(self):
        return "{0}".format(self.name_of_group)


class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    cafedra = models.ForeignKey('Cafedra',on_delete=models.CASCADE)


    def __str__(self):
        return "{0} {1}".format(self.user.first_name,self.user.last_name)

    class Meta:
        permissions=(('can_edit_marks','edit marks'),)


class Cafedra(models.Model):
    name_of_cafedra = models.CharField(max_length=50)
    faculty = models.ForeignKey('Faculty',on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_cafedra


class Faculty(models.Model):
    name_of_faculty = models.CharField(max_length=60)

    def __str__(self):
        return self.name_of_faculty


class Subject(models.Model):
    name = models.CharField(max_length=200,primary_key=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subjects = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    time = models.TimeField(verbose_name='Time')
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return "{0}".format(self.subjects.name)

    def Days(self):
        days = []
        for i in self.day_set.all():

            days.append(int(i.name_of_day))
        return days



class Day(models.Model):

    choices = (
        ('0','Monday'),
        ('1','Tuesday'),
        ('2','Wednesday'),
        ('3','Thursday'),
        ('4','Friday')
    )
    name_of_day = models.CharField(max_length=15,choices=choices)
    lessons = models.ManyToManyField(Lesson)
    date = models.DateField(null=True)
    schedule = models.ForeignKey('Schedule',on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.get_name_of_day_display())

class Schedule(models.Model):
    group = models.OneToOneField(StudentsGroup,on_delete=models.CASCADE)

    def __str__(self):
        return "shedule {0}".format(self.group.name_of_group)

class Semestr(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{0}-{1}".format(self.start_date,self.end_date)


class Journal(models.Model):
    schedule = models.OneToOneField(Schedule,on_delete=models.CASCADE)
    semestr = models.ForeignKey(Semestr,on_delete=models.CASCADE)
    group = models.OneToOneField(StudentsGroup,on_delete=models.CASCADE)

    def __str__(self):
        return "journal {0}".format(self.group.name_of_group)


class Mark(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)

    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    value = models.CharField(max_length=2)
    date = models.DateField()
    rowindex=models.IntegerField()
    colindex=models.IntegerField()

    def __str__(self):
        return "{0} {1}".format(self.date,self.value)

