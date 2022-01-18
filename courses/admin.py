from django.contrib import admin

from courses.models import Course


class CourseAdmin(admin.ModelAdmin):

    list_display = ('nome','slug','created_at','descricao')
    search_fields = ('nome','slug')


admin.site.register(Course,CourseAdmin)
