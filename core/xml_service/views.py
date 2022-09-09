from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import AddSerializer
from .services import format_xml


class AddView(generics.GenericAPIView):
    serializer_class = AddSerializer

    def get(self, request, *args, **kwargs):
        res = format_xml()

        return Response(
            res, content_type='text/xml',
            status=status.HTTP_200_OK,
        )
