from django.contrib import admin
from .models import (Resume,Interest,
                     Education,Skill,Project,
                     Experience,Certification,CompanyOwner,
                     Category,Location,JobPost)
from accounts.models import User

admin.site.register(User)
admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Interest)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(CompanyOwner)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(JobPost)
