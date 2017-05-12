from django.contrib import admin

from .models import StudentFather,StudentMother,StudentSchoolInfo,Student,PaymentInfo,ReminderInfo,Donor

class StudentAdmin(admin.ModelAdmin):
	# list_display = ['first_name','last_name','date_of_admission']
	pass
admin.site.register(Student,StudentAdmin)

class StudentFatherAdmin(admin.ModelAdmin):
	# list_display = ['first_name','last_name']
	pass
admin.site.register(StudentFather,StudentFatherAdmin)

class StudentMotherAdmin(admin.ModelAdmin):
	# list_display = ['first_name']
	pass
admin.site.register(StudentMother,StudentMotherAdmin)

class StudentSchoolInfoAdmin(admin.ModelAdmin):
	# list_display = ['admission_secured_school']
	pass
admin.site.register(StudentSchoolInfo,StudentSchoolInfoAdmin)

class DonorAdmin(admin.ModelAdmin):
	# list_display = ['first_name','last_name']
	pass
admin.site.register(Donor,DonorAdmin)

class PaymentInfoAdmin(admin.ModelAdmin):
	# list_display = ['admission_secured_school']
	pass
admin.site.register(PaymentInfo,PaymentInfoAdmin)

class ReminderInfoAdmin(admin.ModelAdmin):
	# list_display = ['admission_secured_school']
	pass
admin.site.register(ReminderInfo,ReminderInfoAdmin)