from django.contrib import admin
import accounts
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'userid')
admin.site.register(accounts.models.Student, StudentAdmin)

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('user', 'employer_id', 'company_name', 'industry', 'company_reg_no', 'contact_person_name', 'designation', 'email', 'telephone_no', 'location','company_size', 'working_hours', 'dress_code', 'benefits', 'transportation', 
    	'website', 'social_media_link', 'company_overview','mission','vission','logo','header','why_join_us')
admin.site.register(accounts.models.Employer, EmployerAdmin)
