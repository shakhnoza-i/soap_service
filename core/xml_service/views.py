from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import AddSerializer
from .services import format_xml


class AddView(generics.GenericAPIView):
    serializer_class = AddSerializer

    def post(self, request, *args, **kwargs):
        res = format_xml(request.data)
        print(res)
        import pdb
        pdb.set_trace() 

        return Response(
            res, content_type='text/xml',
            status=status.HTTP_200_OK,
        )
