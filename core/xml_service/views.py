from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import AddSerializer
from .services import format_xml


class AddView(generics.GenericAPIView):
    serializer_class = AddSerializer

    def post(self, request, *args, **kwargs):
        print(request)
        print(request.data) # {'{http://schemas.xmlsoap.org/soap/envelope/}Body': {'{http://tempuri.org/}Add': {'{http://tempuri.org/}intA': 8, '{http://tempuri.org/}intB': 15}}}
        res = format_xml(request.data)

        return Response(
            res, content_type='text/xml',
            status=status.HTTP_200_OK,
        )


@api_view(['POST'])
def add_post(request, *args, **kwargs):
    print(request)
    print(request.data)
    res = format_xml(request.data)
    print(res)
    import pdb
    pdb.set_trace() 

    return Response(
        res, content_type='text/xml',
        status=status.HTTP_200_OK,
    )
