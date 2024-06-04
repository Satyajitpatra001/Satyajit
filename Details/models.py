from django.db import models

class Journal(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    image = models.ImageField(upload_to='journal_images/', null=True, blank=True) 

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completion_date = models.DateField()
    image = models.ImageField(upload_to='works/')

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    title = models.CharField(max_length=100, default='We can make it together')
    image = models.ImageField(upload_to='about_me/')
    primary_caption = models.TextField(max_length=500)
    secondary_caption = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class MainDetails(models.Model):
    main_heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    logo_image = models.ImageField(upload_to='logo_image/', blank=True, null=True)
    main_background_image = models.ImageField(upload_to='background_image/')

    def __str__(self):
        return self.main_heading
    
    
    
