from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('manager', 'Manager'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    addr = models.TextField()

    def __str__(self):
        return self.name


class Pet(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    species = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    health_status = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets")

    def __str__(self):
        return self.name


class Announcement(models.Model):
    TYPE_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('adoption', 'Adoption'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('finished', 'Finished'),
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    announcer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="announcements")
    age = models.PositiveIntegerField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="announcements")
    images_path = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.pet.name}"


class CareHouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carehouses")
    addr = models.TextField()
    pets = models.ManyToManyField(Pet, related_name="carehouses")

    def __str__(self):
        return self.name


class Ad(models.Model):
    TYPE_CHOICES = [
        ('general', 'General'),
        ('promotional', 'Promotional'),
        ('event', 'Event'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image_path = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    description = models.TextField()

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    img_path = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    description = models.TextField()

    def __str__(self):
        return self.title
