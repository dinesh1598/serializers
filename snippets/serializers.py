from rest_framework import serializers
from .models import Snippet,LANUGUAGE_CHOICES,STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snippet
        fields=('id','title','language','code','style',)