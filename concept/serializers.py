from rest_framework import serializers
from concept.models import Concept

class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ('title', 'video_url', 'description', 'example', 'notes', 'subject')
