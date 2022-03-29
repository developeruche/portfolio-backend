from django.contrib import admin
from .models import ProjectModal, MessageModal, Technology, Testimonial


admin.site.register((ProjectModal, MessageModal, Testimonial, Technology))
