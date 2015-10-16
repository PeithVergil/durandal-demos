from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password', 'date_created', 'date_updated')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

        read_only_fields = ('date_created', 'date_updated')

    def create(self, validated_data):
        """
        The "create_user" method ensures that the password is hashed.
        """
        return User.objects.create_user(validated_data['username'],
                                        validated_data['password'])