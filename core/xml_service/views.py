from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MathSerializer
from .services import format_xml


class MathView(generics.GenericAPIView):
    serializer_class = MathSerializer

    def post(self, request, *args, **kwargs):
# {'{http://schemas.xmlsoap.org/soap/envelope/}Body': {'{http://tempuri.org/}Add': {'{http://tempuri.org/}intA': 8, '{http://tempuri.org/}intB': 15}}}
        res = format_xml(request.data)

        return Response(
            res, content_type='text/xml',
            status=status.HTTP_200_OK,
        )


@api_view(['POST'])
def add_post(request, *args, **kwargs):
    res = format_xml(request.data)

    return Response(
        res, content_type='text/xml',
        status=status.HTTP_200_OK,
    )
