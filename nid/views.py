from rest_framework import viewsets, permissions, exceptions
from nid.models import NID, NIDUser
from nid.serializers import NIDSerializer, NIDUserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class NIDViewSet(viewsets.ModelViewSet):
    queryset = NID.objects.all()
    serializer_class = NIDSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'verify_nid':
            return [permissions.AllowAny()]
        return super().get_permissions()

    @action(detail=False, methods=['get'], url_path='verify')
    def verify_nid(self, request):
        nid_number = request.query_params.get('nid')

        if not nid_number:
            raise exceptions.ValidationError({'nid': 'NID parameter is required.'})

        try:
            nid_obj = NID.objects.get(nid=nid_number)
            serializer = NIDSerializer(nid_obj)
            return Response(serializer.data)
        except NID.DoesNotExist:
            raise exceptions.NotFound({'error': 'NID not found.'})



class NIDUserViewSet(viewsets.ModelViewSet):
    queryset = NIDUser.objects.all()
    serializer_class = NIDUserSerializer
    permission_classes = [permissions.IsAuthenticated]


from django.shortcuts import render
from .models import NIDUser

def nid_gallery_view(request):
    users = NIDUser.objects.all()
    return render(request, "nid_gallery.html", {"users": users})
