from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo

        fields = (
            'id', 'title', 'status', 'date_created', 'date_updated'
        )

        read_only_fields = (
            'date_created', 'date_updated'
        )
