from app.core.api.generics import ListApiView
from app.core.api.pagination import CustomPagination
from app.subscriptions.api.serializers import CategoryModelSerializer
from app.subscriptions.models import Category


class CategoryListApiView(ListApiView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    pagination_class = CustomPagination
