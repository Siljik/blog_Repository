from rest_framework import serializers

from blog.models import blogModel

class blogserializer(serializers.ModelSerializer):
    class Meta:
        model = blogModel
        fields =(
            'userid',
            'title',
            'message'
        )
        