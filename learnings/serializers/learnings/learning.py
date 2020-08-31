from ..base_imports import *


class LearningSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_author(self, instance):
        return instance.author.profile.get_full_name()

    def get_status(self, instance):
        return instance.get_status()

    class Meta:
        model = Learning
        fields = (
            'id', 'title', 'description', 'is_deleted', 'author', 'status', 'created', 'updated'
        )
    
    