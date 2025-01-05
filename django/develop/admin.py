from django.contrib import admin
from .models import User, Pet, CareHouse, Announcement, Ad, BlogPost

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(CareHouse)
admin.site.register(Announcement)
admin.site.register(Ad)
admin.site.register(BlogPost)