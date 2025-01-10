from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

# User Serializer to handle data conversion:
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_membership','is_active']
        
    def update(self, instance, validated_data):
        # Ensure 'is_active' remains True even when updating other fields
        """
        Update a user instance with new data. Ensures 'is_active' field always remains True.
        If 'password' is being updated, it is hashed before being stored in the database.
        
        Args:
            instance (User): the user instance being updated
            validated_data (dict): the new data to be used for updating the user instance
        Returns:
            User: the updated user instance
        Raises:
            serializers.ValidationError: if 'is_active' is set to False
        """
        is_active = validated_data.get('is_active', instance.is_active)
        
        if not is_active:
            raise serializers.ValidationError("User cannot be inactive.")

        # Handle password hashing if it is being updated
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        # Update the user instance with the new data
        return super().update(instance, validated_data)    