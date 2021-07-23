from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.HyperlinkedRelatedField(
        many=True, view_name='order-detail', read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
