from rest_framework.views import APIView
from rest_framework.response import Response

import requests

from .serializers import BookSerializer

class ListBooks(APIView):

    # Bonus feature: The requirements called for the data to be sortable by title or publication date
    # By implementing sorting generically, we can satisfy the requirement as well as provide functionality to sort by
    # any field in the data!
    def get_sorted_data(self, data, ordering):
        # a '-' at the start of our query parameter indicates we want the order to be reversed
        reverse = ordering[0] is '-'

        # if it is reversed, strip the - off the beginning so our ordering parameter matches the model field name
        if reverse:
            ordering = ordering[1:]

        return sorted(data, key=lambda i: i[ordering], reverse=reverse)

    def get(self, request):
        try:
            req = requests.get('https://hokodo-frontend-interview.netlify.com/data.json')
            json = req.json()

            serializer = BookSerializer(data=json.get('books', ''), many=True)

            if serializer.is_valid():
                data = serializer.data
            else:
                return Response(status=500, data='There was an error reading the data - the format may have changed')
        except:
            return Response(status=500, data='There was an error fetching the data - the service may be unavailable')

        if 'ordering' in request.query_params:
            data = self.get_sorted_data(data, request.query_params['ordering'])

        return Response(data)


