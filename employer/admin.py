from django.contrib import admin
import employer
# Register your models here.

class EmployerJobAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'role', 'location', 'responsibilities', 'requirements', 'how_to_apply', 'salary', 'post_date', 'deadline')
admin.site.register(employer.models.EmployerJob, EmployerJobAdmin)
