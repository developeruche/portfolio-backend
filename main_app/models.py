from django.db import models

# Create your models here.
class GenericFileUpload(models.Model):
    """ This route would be used for uploading images, pdf and any other media file this would also handle downloadinf of this uploaded files """
    file_upload = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_upload} created at {self.created_at}"

class VideoUpload(models.Model):
    """ This is a model that would be responsible for uploading the project videos """
    video_upload = models.FileField(upload_to="videos")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.video_upload} created at {self.created_at}"


class Technology(models.Model):
    """ This model would just hold and display a string of the tech the application is built on """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProjectModal(models.Model):
    """ This model would handle this uploading of portfolio data (img, text) """
    developer = models.CharField(default="@developeruche", max_length=115)
    image = models.ForeignKey(GenericFileUpload, related_name="projects_image", null=True, on_delete=models.SET_NULL)
    source_code = models.ForeignKey(GenericFileUpload, related_name="projects_source_code", null=True, on_delete=models.SET_NULL) #This would be the link of source code which would avaliable for download and handle with the react frontend
    demo_url = models.CharField(max_length=300) #This field would hold the link to this project server ip addr
    long_description = models.TextField()
    short_description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    tech = models.ManyToManyField(Technology)
    video = models.ForeignKey(VideoUpload, related_name="project_video", null=True, on_delete=models.SET_NULL)
    main_image = models.ForeignKey(GenericFileUpload, related_name="project_main_image", null=True, on_delete=models.SET_NULL)
    github = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        # I want the ordering of the data to be in order of desending other with time(when it was created)
        ordering = ("created_at",)


class Testimonial(models.Model):
    """ This  model would carter for the testimonial from my client """
    pics = models.ForeignKey(GenericFileUpload, related_name="testimonial_picture", null=True, on_delete=models.SET_NULL)
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


