
from django.contrib import admin
from simpleFirstApp.models import Students,Teachers,Courses,Subjects,StudentSubjects


admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(StudentSubjects)