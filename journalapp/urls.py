from django.urls import path,re_path
from .views import *

urlpatterns=[
    path('faculties/',FacultiesListView.as_view(),name='faculties'),
    path('faculties/<int:pk>/',FacultyView,name='Faculty_Detail'),
    path('faculties/groups/',get_group_by_cafedra, name='get_groups_by_cafedra'),
    path('faculties/all_groups/',get_all_groups_in_faculty_in_json, name='get_all_groups_in_faculty'),
    path('all_groups/<int:pk>/', group_view, name='group_view'),
    path('schedules/<int:pk>/',schedule_view,name='schedule'),
    path('journal/<int:jpk>/',journal_view,name='journal_view'),
    path('journal/marks/',get_all_marks_by_enter,name='get_all_marks'),
    path('journal/all_marks/',get_all_marks,name = 'marks')



]