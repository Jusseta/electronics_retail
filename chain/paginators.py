from rest_framework.pagination import PageNumberPagination


class RetailChainPaginator(PageNumberPagination):
    page_size = 20
