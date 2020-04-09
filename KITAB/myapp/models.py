from django.db import models
from django.contrib.auth.models import User #Accessing User module from admin portal
from django.utils import timezone
from django.urls import reverse

# Extend User Details

class UserDet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document = models.ImageField(upload_to='profilepic/',)
    dob = models.DateField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
# create user profile


class UserProfile(models.Model):

    ############### Choices############
    gender_choice = [('Male','Male'),('Female','Female'),]
    occupation_choice = [('Student','Student'),('Government Employee','Government Employee'),
                            ('Engineer','Engineer'),('Doctor','Doctor'),('Accountant','Accountant'),
                            ('Office Assistant','Office Assistant'),('Sales Man','Sales Man'),
                            ('Own Business','Own Business'),('Painter','Painter'),('Welder/Wiring','Welder/Wiring'),
                            ('Drughman','Drughman'),('Office Boy','Office Boy'),('Others','Others'),]
    blood_choice = [('O+ve','O+ve'),('O-ve','O-ve'),('A+ve','A+ve'),('A-ve','A-vve'),('B+ve','B+ve'),('B-ve','B-ve'),('AB+ve','AB+ve'),('AB-ve','AB-ve'),]
    marital_choices = [('Married','Married'),('Single','Single'),('Divorced','Divorced'),('Widowed','Widowed'),]



    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    # date_of_birth = models.DateField(max_length = 15)
    gender = models.CharField(max_length = 100,choices=gender_choice)
    father_name = models.CharField(max_length = 100)
    mother_name = models.CharField(max_length = 100)
    add_line1 = models.CharField(max_length = 300,verbose_name="House name/number")
    add_line2 = models.CharField(max_length = 300,blank=True,null=True,verbose_name="Locality and Villege")
    add_line3 = models.CharField(max_length = 300,blank=True,null=True,verbose_name="District and State")
    occupation = models.CharField(max_length = 100,choices=occupation_choice,blank=True)
    adhaar = models.CharField(max_length = 100,verbose_name="ADHAAR Number",blank=True)
    mobile = models.CharField(max_length = 100)
    blood_group = models.CharField(max_length = 100,choices=blood_choice)
    marital_status = models.CharField(max_length = 100,choices=marital_choices,blank=True)
    created_date = models.DateTimeField(default=timezone.now())
    modified_date = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def modified(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
         return self.user.username

class UserEduDetails(models.Model):
    qual_choices = [('Mba','Mba'),('btech','B.tech'),('mtech','M.tech'),('bsc','B.Sc'),('msc','M.Sc'),('bca','B.Ca'),('mca','M.Ca'),('bbm','BBM'),('BBA','BBA'),
                    ('ttm','TTM'),('mttm','MTTM'),('ba','B.A'),('ma','M.A'),('polytechnic','Poly Technic (3 Year)'),('iti one year','ITI (1 Year)'),('iti 6 month','ITI (6 Month)'),
                    ('iti 2 year','ITI (2 Year)'),('phd','Ph.D'),('Mphil','M.phil'),('plus2','Plus Two'),('sslc','SSLC'),('7std','7 Standerd'),
                    ('below7','Below 7 Standerd'),('Others','Others'),]
    stream_choice = [('Science','Science'),('Commerce','Commerce'),('Arts','Arts'),('Certification','Certification'),('Special Course','Special Course'),]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification1 = models.CharField(max_length = 100,verbose_name="Highest Qualification",choices=qual_choices)
    qual1_stream = models.CharField(max_length = 100,verbose_name="Stream",choices=stream_choice)
    qual1_sub = models.CharField(max_length = 100,verbose_name="Subject",blank=True)
    qual1_pass_year = models.DateField(max_length = 15,verbose_name="Year of Pass",blank=True)
    qual1_college = models.CharField(max_length = 100,verbose_name="College/University",blank=True)
    qualification2 = models.CharField(max_length = 100,verbose_name="Secondary Qualification",choices=qual_choices,blank=True)
    qual2_stream = models.CharField(max_length = 100,verbose_name="Stream",choices=stream_choice,blank=True)
    qual2_sub = models.CharField(max_length = 100,verbose_name="Subject",blank=True)
    qual2_pass_year = models.DateField(max_length = 15,verbose_name="Year of Pass",blank=True)
    qual2_college = models.CharField(max_length = 100,verbose_name="College/University",blank=True)
    created_date = models.DateTimeField(default=timezone.now())
    modified_date = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def modified(self):
        self.modified_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def __str__(self):
         return self.user.username


class UserSkillDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length = 100,blank = True)
    skill = models.CharField(max_length = 100)
    work_location = models.CharField(max_length = 100)
    company_name = models.CharField(max_length = 100)
    work_exp = models.CharField(max_length = 100,verbose_name="Total Work Experience")
    expertise = models.CharField(max_length = 100)
    created_date = models.DateTimeField(default=timezone.now())
    modified_date = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def modified(self):
        self.modified_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def __str__(self):
         return self.user.username
