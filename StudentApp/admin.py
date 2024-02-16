from django.contrib import admin
from .models import Student
from .models import Profesor
from .models import Curso

# Register your models here.
admin.site.register(Student)
admin.site.register(Profesor)
admin.site.register(Curso)

