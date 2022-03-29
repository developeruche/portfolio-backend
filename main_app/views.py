# This is where most of the algorithm would take place
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ( ProjectModal, 
                        ProjectModalSerializer, TestimonialSerializer, Testimonial, MessageModal, MessageSerializer)
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status



class ProjectView(ModelViewSet):
    """ The image and the source code would be posted first on admin page then id would be retrieved for the api pourpose """
    queryset = ProjectModal.objects.all()
    serializer_class = ProjectModalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ) #This way an outside will not just come to the rest frame work provided interface and manipluate data instead data cxan be controlled by the authenticated user via the django admin platform





class ProjectPaginated(ModelViewSet):
    """ The View would manually carter for any paginated request of any such """
    queryset = ProjectModal.objects.all()
    serializer_class = ProjectModalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ) 


    def get_queryset(self):
        data = self.request.query_params.dict()
        start = data.get("start", 0)
        contain = data.get("contain", 4)
        page = int(start) + int(contain)

        return self.queryset[int(start):page]




class TestimonialView(ModelViewSet):
    """ This view would download testimonial """
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ) 


class MessageView(ModelViewSet):
    queryset = MessageModal.objects.all()
    serializer_class = MessageSerializer


