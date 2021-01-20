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
    photo = models.FileField(upload_to='resume/',null=True)
    name = models.CharField(max_length=255)
    professional_title = models.CharField(max_length=255,default='')
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
    ('Full Time','F'),
    ('Part Time','P'),
    ('Other','O')
}


class JobPost(models.Model):
    photo = models.FileField(upload_to='media/jobs/',null=True)
    posted_by = models.ForeignKey(CompanyOwner,on_delete=models.CASCADE)
    job_category = models.ForeignKey(Category,related_name="job_cats",on_delete=models.CASCADE)
    job_type = models.CharField(choices=TYPES,max_length=255)
    title = models.CharField(max_length=255)
    locations = models.CharField(max_length=255)
    requirements = models.TextField()
    description = models.TextField(max_length=255)
    salary = models.CharField(max_length=100)
    experience = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_date = models.CharField(max_length=100,default='')

    def __str__(self):
        return f"{self.title} and id {self.id}"


class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)

# e = mod