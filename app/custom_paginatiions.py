from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                'ok':True,
                "members": data,
            }
        )
