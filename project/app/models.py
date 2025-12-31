from django.db import models  # Import models module to create database tables

# ============================
# Student Model
# ============================
class Student(models.Model):

    Name = models.CharField(max_length=50)  # CharField for storing short text like Name, max_length is required
    Email = models.EmailField()              # EmailField automatically validates proper email format
    Contact = models.IntegerField()          # IntegerField for storing numeric contact number (leading zeros not allowed)
    Details = models.CharField(max_length=100)  # CharField for short additional info about student
    Image = models.ImageField(upload_to='image/')  # ImageField to upload image, stored in media/image/
    Password = models.CharField(max_length=30, null=True)  # CharField for password, allows null

    # __str__ method returns a readable representation of object in admin panel
    def __str__(self):
        return self.Name  # Returning contact number as string; you can also return Name