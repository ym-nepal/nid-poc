from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import NID
from .serializers import NIDSerializer

class NIDViewSet(viewsets.ModelViewSet):
    serializer_class = NIDSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return NID.objects.filter(user=self.request.user)
    
    def get_permissions(self):
        if self.action == 'verify_nid':
            return [permissions.AllowAny()]
        return super().get_permissions()

    @action(detail=False, methods=['post'], url_path='verify')
    def verify_nid(self, request):
        permissions_classes = [permissions.AllowAny]
        input_nid = request.data.get('nid')
        if not input_nid:
            return Response({'error': 'NID not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            nid_record = NID.objects.get(nid=input_nid)
            # Optional: Check if it's owned by the current user
            # if nid_record.user != request.user:
            #     return Response({'detail': 'Not authorized to view this NID'}, status=status.HTTP_403_FORBIDDEN)

            serializer = self.get_serializer(nid_record)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NID.DoesNotExist:
            return Response({'detail': 'NID not found'}, status=status.HTTP_404_NOT_FOUND)
