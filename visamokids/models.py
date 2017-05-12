from django.db import models

# Create your models here.


# Personal Details of Father
class StudentFather(models.Model):
	first_name = models.CharField(max_length=100, help_text="e.g. Sumanbhai", blank=True, null=True)
	middle_name = models.CharField(max_length=100, help_text="e.g. Nenadiya",blank=True, null=True)
	last_name = models.CharField(max_length=100, help_text="e.g. Gamit", blank=True, null=True)
	education_of_father = models.CharField(max_length=300, blank=True, null=True, help_text="e.g. Studied till 10th grade")
	occupation_of_father = models.CharField(max_length=300, blank=True, null=True, help_text="e.g. Business")
	contact_number = models.BigIntegerField(blank=True, null=True, help_text="e.g. 8844999000")
	address = models.TextField(blank=True, null=True, help_text="e.g. 8 Gomatipur Street, Sarkhej")
	district = models.CharField(max_length=300, blank=True, null=True, help_text="e.g. Ahmedabad")
	monthly_income = models.BigIntegerField(blank=True, null=True, help_text="e.g. 1333")


	def __unicode__(self):
		return "{0} {1}".format(self.first_name, self.last_name)

# Personal details of Mother of the child
class StudentMother(models.Model):
	first_name = models.CharField(max_length=100, help_text="e.g. Anitaben",blank=True, null=True)
	education_of_mother = models.CharField(max_length=300,blank=True, null=True, help_text="e.g. Studied till 10th grade")
	occupation_of_mother = models.CharField(max_length=300,blank=True, null=True, help_text="e.g. Business")
	contact_number = models.BigIntegerField(blank=True, null=True, help_text="e.g. 8844999000")
	monthly_income = models.BigIntegerField(blank=True, null=True, help_text="e.g. 1333")


	def __unicode__(self):
		return str(self.first_name)

# School related information
class StudentSchoolInfo(models.Model):
	admission_secured_school = models.CharField(max_length=300,blank=True, null=True, help_text="e.g. Anand Niketan School")
	date_of_admission_in_school = models.DateField(blank=True, null=True)
	school_enrollment_number = models.BigIntegerField(blank=True, null=True, help_text="e.g. 41")
	aadhar_card_no = models.BigIntegerField(blank=True, null=True, help_text="e.g. 957877658493")
	GRADE_TYPE_CHOICES = (
		('1', '1st Grade'),
		('2', '2nd Grade'),
		('3', '3rd Grade'),
		('4', '4th Grade'),
		('5', '5th Grade'),
		('6', '6th Grade'),
		('7', '7th Grade'),
		('8', '8th Grade'),
		('9', '9th Grade'),
		('10', '10th Grade'),
		('11', '11th Science'),
		('11', '11th Commerce'),
		('12', '12th Science'),
		('12', '12th Commerce'),
	)
	grade = models.CharField(choices = GRADE_TYPE_CHOICES, default = '1', max_length=3, blank=True, null=True)
	STATUS_TYPE_CHOICES = (
		('STU', 'Studying'),
		('DRP', 'Drop Out'),
		('PSD', 'Passed Out'),
	)
	status = models.CharField(choices=STATUS_TYPE_CHOICES, default='STU', max_length=3, blank=True, null=True)

	def __unicode__(self):
		return str(self.admission_secured_school)

class Student(models.Model):
	# Detailed information	of the	student
	gr_no = models.BigIntegerField(help_text="e.g. 39", primary_key=True, default=0)
	first_name = models.CharField(max_length=100, help_text="e.g. Arpit", blank=True, null=True)
	middle_name = models.CharField(blank=True, null=True, max_length=100, help_text="e.g. Sumanbhai")
	last_name = models.CharField(max_length=100, help_text="e.g. Gamit",blank=True, null=True)
	dob = models.DateField(blank=True, null=True)
	birth_place = models.CharField(max_length=300, blank=True, null=True, help_text="e.g. Uchhal ,Surat")
	bio = models.TextField(blank=True, null=True, help_text="e.g. Has four siblings. Two younger and two elder ones.. or.. Started working as developer in TCS.")
	caste = models.CharField(max_length=300, blank=True, default='None', null=True,help_text="e.g. Hindu Gamit")
	SC_ST_OBC_CHOICES = (
		('SC','SC'),
		('ST','ST'),
		('OBC','OBC'),
		('OTHER','Other'),
		)
	
	sc_st_obc = models.CharField(choices = SC_ST_OBC_CHOICES, default = 'OTHER', max_length=5)
	nationality = models.CharField(max_length=300, blank=True, null=True, help_text="e.g. Indian")
	blood_group = models.CharField(blank=True, null=True, max_length=10, help_text="e.g. O+ve")
	date_of_admission = models.DateField()
	
	YES = 'Yes'
	NO = 'No'
	YES_NO_CHOICES = (
		(YES,'Yes'),
		(NO,'No'),
		)
	medical_report = models.CharField(choices = YES_NO_CHOICES, default = NO, max_length=3)
	findings = models.CharField(max_length=300, blank=True, null=True)
	iq_test = models.CharField(choices = YES_NO_CHOICES, default = NO, max_length=3)
	iq_result = models.IntegerField(blank=True, null=True,help_text="e.g. 98")

	# Personal Details of Father
	father_of_student = models.ForeignKey(StudentFather, on_delete=models.CASCADE, blank=True, null=True)
	# Personal details of Mother of the child
	mother_of_student = models.ForeignKey(StudentMother, on_delete=models.CASCADE, blank=True, null=True)
	# School related information
	student_school_info = models.ForeignKey(StudentSchoolInfo, on_delete=models.CASCADE, blank=True, null=True)

	def __unicode__(self):
		return "{0} {1}".format(self.first_name, self.last_name)

# Payment related information
class PaymentInfo(models.Model):
	sponsorship_amount = models.BigIntegerField(blank=True, null=True, help_text="e.g. 3,60,000")
	sponsorship_date = models.DateField(blank=True, null=True)
	payment_details = models.TextField(blank=True, null=True,
						   help_text="e.g. Payment done with Paytm App. Amount credited to Paytm Number 9999888800. Amount credited is Rs 2,00,000.")
	def __unicode__(self):
		return str(self.sponsorship_date)

# Reminder related information
class ReminderInfo(models.Model):
	YES_NO_CHOICES = (
		('Y', 'Yes'),
		('N', 'No'),
	)
	reminder_sent_flag = models.CharField(choices=YES_NO_CHOICES, default='Y', max_length=3, blank=True, null=True)
	reminder_date = models.DateField(blank=True, null=True)
	reminder_comments = models.TextField(blank=True, null=True, help_text="Reminder sent to Pradeep")

	def __unicode__(self):
		return str(self.reminder_date)

class Donor(models.Model):
	# Personal details of the sponsor / donor
	first_name = models.CharField(max_length=100, help_text="e.g. Pradeep", blank=True, null=True)
	last_name = models.CharField(max_length=100, help_text="e.g. Khandwala", blank=True, null=True)
	contact_number = models.BigIntegerField(blank=True, null=True, help_text="e.g. 8844999000")
	email = models.EmailField(blank=True, null=True, help_text="e.g. pradeep@factory.com")
	dob = models.DateField(blank=True, null=True)
	dob_family_member = models.DateField(blank=True, null=True)
	marriage_anniversary = models.DateField(blank=True, null=True)
	address = models.TextField(blank=True, null=True, help_text="e.g. 8 Gomatipur Street, Sarkhej")
	citizenship = models.CharField(max_length=100, help_text="e.g. Indian, US Citizen", blank=True, null=True)
	# Details of Sponsorship
	child_sponsored = models.ManyToManyField(Student, related_name='student')
	# Sponsorship Amount related information
	payment_info = models.ManyToManyField(PaymentInfo, related_name='payment_info')

	SPNSR_TYPES_CHOICES = (
		('IND', 'Individual'),
		('GRP', 'Group'),
		('INS', 'Institutional'),
		('CSR', 'CSR'),
	)
	sponsorship_type = models.CharField(choices = SPNSR_TYPES_CHOICES, default = 'IND', max_length=3, blank=True, null=True)
	SPNSR_SUB_TYPES_CHOICES = (
		('CMPLT', 'Complete Sponsorship'),
		('ANNUL', 'Annual Sponsorship For Education'),
		('SBFC', 'Sponsor Boarding, Food, Clothes'),
		('SM', 'Sponsor a Child\'s Meals'),
		('SB', 'Sponsor a Child\'s Boarding'),
		('SDM', 'Sponsor a Days\'s Meal'),
		('TD', 'Token Donation'),
		('IK', 'In Kind'),
	)
	sponsorship_sub_type = models.CharField(choices=SPNSR_SUB_TYPES_CHOICES, default='CMPLT', max_length=5, blank=True, null=True)
	in_kind_donation = models.TextField(help_text="e.g. In Kind Donation", blank=True, null=True)
	SPNSR_NATURE_CHOICES = (
		('REG', 'Regular Donor'),
		('NEW', 'New Donor'),
	)
	sponsorship_nature = models.CharField(choices = SPNSR_NATURE_CHOICES, default = 'REG', max_length=3, blank=True, null=True)
	YES_NO_CHOICES = (
		('Y', 'Yes'),
		('N', 'No'),
	)
	# Tax Exemption
	is_35_ac_given = models.CharField(choices=YES_NO_CHOICES, default='Y', max_length=3 , blank=True, null=True)
	is_80_G = models.CharField(choices=YES_NO_CHOICES, default='Y', max_length=3, blank=True, null=True)
	# Reference
	reference = models.CharField(max_length=100, help_text="e.g. Pradeep", blank=True, null=True)
	# Reminder Detail information
	reminder_info = models.ManyToManyField(ReminderInfo, related_name='reminder_info')

	# Documents Shared with Donors
	child_pictures_available = models.CharField(choices=YES_NO_CHOICES, default='Y', max_length=3, blank=True, null=True)
	child_story_available = models.CharField(choices=YES_NO_CHOICES, default='Y', max_length=3, blank=True,	null=True)
	progress_report = models.CharField(choices=YES_NO_CHOICES, default='Y', max_length=3, blank=True, null=True)
	annual_report = models.CharField(choices=YES_NO_CHOICES, default='Y', max_length=3, blank=True, null=True)

	def __unicode__(self):
		return "{0} {1}".format(self.first_name, self.last_name)