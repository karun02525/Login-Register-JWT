from django.urls import path
from .views import ProductAPI,RegisterUser,ProductGeneric,UpdateProductGeneric,LoginUser

urlpatterns = [
    path('products',ProductAPI.as_view(), name='Products'),
    path('register',RegisterUser.as_view(), name='Register'),
    path('login',LoginUser.as_view(), name='LoginUser'),
    
    path('generic-product',ProductGeneric.as_view(), name='Generic Product'),
    path('generic-product/<id>',UpdateProductGeneric.as_view(), name='Update Product'),
    
]
    # path('product',product, name='product'),
    # path('products',products,name='product'),
    # path('add-product',add_product,name='Add Product'),
    # path('update-product/<id>',update_product,name='Update Product'),
    # path('delete-product/<id>',delete_product,name='Delete Product'),
    # path('get-book',get_books,name='Get Book'),

