from django.contrib import admin
from .models import GenericFileUpload, ProjectModal, MessageModal, Technology, Testimonial, VideoUpload


admin.site.register((GenericFileUpload, ProjectModal, MessageModal, Testimonial, Technology, VideoUpload))
