from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.


class FacultiesListView(generic.ListView):
    model = Faculty
    template_name = 'journalapp/faculties.html'

def FacultyView(request,pk):

    faculty = Faculty.objects.all().get(pk=pk)
    name = faculty.name_of_faculty
    cafedras = faculty.cafedra_set.all()
    print(request)
    return render(request,"journalapp/Faculty_Detail.html",{'name':name,'cafedras':cafedras})


def get_group_by_cafedra(request):

    name_of_cafedra = request.GET.get('name_of_cafedra')


    cafedra = Cafedra.objects.get(name_of_cafedra__exact=name_of_cafedra)
    queryset = serializers.serialize('json',cafedra.studentsgroup_set.all())


    data = {
        'groups': queryset
    }


    return JsonResponse(data, safe=True)

def get_all_groups_in_faculty_in_json(request):

    name_of_faculty = request.GET.get('name_of_faculty')
    faculty = Faculty.objects.get(name_of_faculty=name_of_faculty)

    cafedras = faculty.cafedra_set.all()

    query=[]
    for cafedra in cafedras:
        groups=cafedra.studentsgroup_set.all()
        for i in groups:
            query.append(i)



    queryset = serializers.serialize('json',query)

    data = {
        'groups': queryset
    }

    return JsonResponse(data, safe=True)


def group_view(request,pk):
    group = StudentsGroup.objects.get(pk=pk)

    name = group.name_of_group
    cafedra_name = group.cafedra.name_of_cafedra
    faculty_name = group.cafedra.faculty.name_of_faculty
    students = group.student_set.all()
    schedule = group.schedule
    journal = group.journal


    return render(request,"journalapp/Group_Detail.html",{'name':name,'cafedra_name':cafedra_name,
                                                          'faculty_name':faculty_name,'students':students,
                                                          'schedule':schedule,'journal':journal})


def schedule_view(request,pk):
    schedule = Schedule.objects.get(pk=pk)
    days = schedule.day_set.all()

    return render(request,"journalapp/schedule.html", {'schedule':schedule,'days':days})


@login_required
def journal_view(request,jpk):
    journal = Journal.objects.get(pk=jpk)
    group = journal.group
    students = journal.group.student_set.all()
    semestr = journal.semestr
    startdate = semestr.start_date
    enddate = semestr.end_date
    schedule = journal.schedule
    days = schedule.day_set.all()
    lessons= set()
    dates = []
    for day in days:
        for lesson in day.lessons.all():
            lessons.add(lesson)

    while startdate != enddate:
        if startdate.weekday() != 5 and startdate.weekday() != 6:
            dates.append(startdate)
        startdate += datetime.timedelta(days=1)

    marks=[]
    for st in group.student_set.all():
        for i in st.mark_set.all():
            marks.append(i)
    print(marks)
    return render(request,"journalapp/journalview.html",{'dates':dates,'students':students,
                                                         'lessons':lessons,'group':group,'marks':marks})



def get_all_marks_by_enter(request):
    value = request.GET.get('value')
    subject_name = request.GET.get('subject')
    colindex = int(request.GET.get('colindex'))
    rowindex = int(request.GET.get('rowindex'))
    day = int(request.GET.get('day'))
    mounth = int(request.GET.get('mounth'))
    year = int(request.GET.get('year'))
    group_name = request.GET.get('group')
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')

    group = StudentsGroup.objects.get(name_of_group=group_name)
    schedule = group.schedule
    date = datetime.date(year=year,month=mounth,day=day)


    subject = Subject.objects.get(pk=subject_name)
    student = group.student_set.get(user__first_name=first_name,user__last_name=last_name)
    if value=='' or value==' ':
        Marks = Mark.objects.filter(student=student,date=date,subject=subject)
        for i in Marks.all():
            i.delete()
    else:
        mark,result = Mark.objects.get_or_create(subject=subject,student=student,date=date,colindex=colindex,
                                                 rowindex=rowindex)
        mark.value = value
        mark.save()



    students = group.student_set.all()
    marks=[]
    for st in students:
        stmarks = st.mark_set.all()
        for m in stmarks:
            marks.append(m)
    marks = serializers.serialize('json',marks)

    data={
        'marks':marks,
    }
    return JsonResponse(data)



def get_all_marks(request):
    group_name = request.GET.get('group')

    group = StudentsGroup.objects.get(name_of_group=group_name)

    students = group.student_set.all()

    marks =[]

    for st in students:
        stmarks = st.mark_set.all()
        for m in stmarks:
            marks.append(m)
    marks = serializers.serialize('json',marks)

    data={
        'marks': marks,
    }
    return JsonResponse(data)
