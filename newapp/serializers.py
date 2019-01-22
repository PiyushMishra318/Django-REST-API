from rest_framework import serializers
from newapp.models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ( 'id',
                  'title', 'code', 'linenos', 'language', 'style')
