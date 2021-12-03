from rest_framework import serializers
from .models import Job


class CreateJobSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=200)
    data = serializers.JSONField(required=True)

    def create(self, validated_data):
        return Job.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class ListJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            "id",
            "name",
            "data",
            "status",
            "result"
        )
