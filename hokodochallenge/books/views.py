from rest_framework.views import APIView
from rest_framework.response import Response

from .book_utils import get_books, sort_data


class ListBooks(APIView):

    def get(self, request):
        try:
            data = get_books()
        except Exception as exc:
            return Response(status=500, data=str(exc))

        if 'ordering' in request.query_params:
            data = sort_data(data, request.query_params['ordering'])

        return Response(data)


# noinspection PyUnusedLocal
class ListAuthors(APIView):
    def get(self, request):
        try:
            data = get_books()
        except Exception as exc:
            return Response(status=500, data=str(exc))

        authors = {}

        for book in data:
            if book['author'] not in authors:
                authors[book['author']] = [book]
            else:
                authors[book['author']].append(book)

        # If a list of objects is preferred with keys 'name' and 'books' for each author, uncomment the following line:
        # authors = [{'name': k, 'books': v} for k, v in authors.items()]

        return Response(authors)
