from django.urls import path, include

from . import views
app_name='ecommerceapp'
urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('<slug:cat_slug>/',views.allProductCat,name='products_by_category'),
    path('<slug:cat_slug>/<slug:product_slug>/',views.prodetail,name='prodCatdetail')

]