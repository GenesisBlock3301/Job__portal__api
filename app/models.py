from accounts.models import *


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()

    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Interest(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    institute_name = models.CharField(max_length=1000)
    grade = models.CharField(max_length=10, blank=True, null=True)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

    def __str__(self):
        return self.institute_name


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='media')
    role = models.CharField(max_length=255)
    github = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)
    university = models.ManyToManyField(Education)
    experience = models.ManyToManyField(Experience)
    skills = models.ManyToManyField(Skill)
    project = models.ManyToManyField(Project)
    certification = models.ManyToManyField(Certification)
    interest = models.ManyToManyField(Interest)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Location(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

    def __str__(self):
        return self.city


TYPES = {
    ('F','Full Time'),
    ('P','Part Time'),
    ('O','Other')
}


class JobPost(models.Model):
    posted_by = models.ForeignKey(CompanyOwner,on_delete=models.CASCADE)
    job_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    job_type = models.CharField(choices=TYPES,max_length=255)
    title = models.CharField(max_length=255)
    locations = models.ForeignKey(Location,related_name='job_posts',on_delete=models.CASCADE)
    requirements = models.TextField()
    description = models.TextField(max_length=255)
    salary = models.DecimalField(max_digits=20,decimal_places=2)
    experience = models.CharField(max_length=255)

    def __str__(self):
        return self.title
