from django.contrib import admin
from .models import Person, Pet, CareHouse

admin.site.register(Person)
admin.site.register(Pet)
admin.site.register(CareHouse)