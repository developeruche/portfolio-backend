from rest_framework import serializers
from .models import MessageModal, ProjectModal, Technology, Testimonial


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"


class ProjectModalSerializer(serializers.ModelSerializer):
    tech = TechnologySerializer(many=True, read_only=True)
    class Meta:
        model = ProjectModal
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModal
        fields = "__all__"
