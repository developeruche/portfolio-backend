from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import GenericFileUploadView, ProjectView, ProjectPaginated, TestimonialView, MessageView

router = DefaultRouter(trailing_slash=False)

router.register("file-upload", GenericFileUploadView)
router.register("projects", ProjectView)
router.register("project-control", ProjectPaginated)
router.register("testimonial/", TestimonialView)
router.register("messageme/", MessageView)


urlpatterns = [
    path("", include(router.urls)),
]
