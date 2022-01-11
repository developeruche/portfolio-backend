from rest_framework import serializers
from .models import GenericFileUpload, MessageModal, ProjectModal, Technology, Testimonial, VideoUpload


class GenericFileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenericFileUpload
        fields = "__all__"

class VideoUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoUpload
        fields = "__all__"

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"


class ProjectModalSerializer(serializers.ModelSerializer):
    # developer = serializers.CharField()
    image = GenericFileUploadSerializer(read_only=True)
    image_id = serializers.IntegerField(
        write_only=True, required=False)
    source_code = GenericFileUploadSerializer(read_only=True)
    source_code_id = serializers.IntegerField(
        write_only=True, required=False)
    tech = TechnologySerializer(read_only=True, many=True)
    video = VideoUploadSerializer(read_only=True)
    video_id = serializers.IntegerField(
        write_only=True, required=False)
    main_image = GenericFileUploadSerializer(read_only=True)
    main_image_id = serializers.IntegerField(
        write_only=True, required=False)

    # demo_url = serializers.CharField()
    # long_description = serializers.CharField()
    # short_description = serializers.CharField()
    # title = serializers.CharField()


    class Meta:
        model = ProjectModal
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    pics = GenericFileUploadSerializer(read_only=True)
    pics_id = serializers.IntegerField(
        write_only=True, required=False)
    class Meta:
        model = Testimonial
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModal
        fields = "__all__"
