from ..base_imports import *


class LearningsList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classses = [permissions.IsAdminUser]

    def get(self, request, format=None):
        learnings = Learning.objects.all()
        serializer = LearningSerializer(learnings, many=True)
        return Response(serializer.data)