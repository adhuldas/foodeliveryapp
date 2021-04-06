from django.urls import path
from . import views

app_name="foodapp"
urlpatterns=[
    path('',views.allProdcat,name='allProdcat'),
    path('<slug:c_slug>/',views.allProdcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.catdetail, name='catdetail')

]