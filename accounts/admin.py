from django.contrib import admin
import accounts
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'userid')
admin.site.register(accounts.models.Student, StudentAdmin)

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('user', 'employerid', 'company_name', 'industry', 'company_reg_no', 'contact_person_name', 'designation', 'email', 'telephone_no', 'location')
admin.site.register(accounts.models.Employer, EmployerAdmin)