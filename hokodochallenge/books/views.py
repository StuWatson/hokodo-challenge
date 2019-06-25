from rest_framework.views import APIView
from rest_framework.response import Response

import requests

from .serializers import BookSerializer


class ListBooks(APIView):

    def get(self, request):
        req = requests.get('https://hokodo-frontend-interview.netlify.com/data.json')
        json = req.json()

        serializer = BookSerializer(data=json['books'], many=True)

        if serializer.is_valid():
            return Response(serializer.data)

