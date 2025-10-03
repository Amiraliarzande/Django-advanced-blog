from django_filters import FilterSet, NumberFilter
from blog.models import Post

class PostPriceFilter(FilterSet):

    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Post
        fields = []