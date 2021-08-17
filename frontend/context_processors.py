from product.models import ProductCategory

def config(request):

    categories = ProductCategory.objects.filter(category_parent__isnull=True)
    return {'categories':categories}
