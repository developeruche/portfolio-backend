from django.db import models

class Technology(models.Model):
    """ This model would just hold and display a string of the tech the application is built on """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProjectModal(models.Model):
    """ This model would handle this uploading of portfolio data (img, text) """
    developer = models.CharField(default="@developeruche", max_length=115)
    image = models.CharField(max_length=500)
    source_code = models.CharField(max_length=500)
    demo_url = models.CharField(max_length=300) #This field would hold the link to this project server ip addr
    long_description = models.TextField()
    short_description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    tech = models.ManyToManyField(Technology)
    video = models.CharField(max_length=500)
    main_image = models.CharField(max_length=500)
    github = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        # I want the ordering of the data to be in order of desending other with time(when it was created)
        ordering = ("created_at",)


class Testimonial(models.Model):
    """ This  model would carter for the testimonial from my client """
    pics = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    no_star = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        # I want the ordering of the data to be in order of desending other with time(when it was created)
        ordering = ("-created_at",)



class MessageModal(models.Model):
    """ This model would handle the stored of message sent to me from my website"""
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    project = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


