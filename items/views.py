from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from items.models import Item


@api_view(http_method_names=['GET'])
def get_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    return Response({
        'id': item.id,
        'title': item.title,
        'description': item.description,
        'image': f'http://{request.get_host()}{item.image.url}',
        'weight': item.weight,
        'price': item.price
    })
