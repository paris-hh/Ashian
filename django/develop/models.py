from django.db import models


class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_info = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    pets = models.ManyToManyField('Pet', related_name='owners', blank=True)

    def __str__(self):
        return self.name


class Pet(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='pets')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class CareHouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    pets = models.ManyToManyField(Pet, related_name='care_houses', blank=True)
    manager = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='managed_care_houses')
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name