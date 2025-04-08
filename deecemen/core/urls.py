from django.urls import path
from .import views



urlpatterns = [

    path('', views.home, name='home'),
    path('login', views.u_login, name='login'),
    path('signup', views.u_signup, name='signup'),
    path('profile',views.profile, name='profile'),
    path('logout', views.u_logout, name='logout'),
    path('men_category', views.men_category, name='men_category'),
    path('women_category', views.women_category, name='women_category'),
    path('kids_category', views.kids_category, name='kids_category'),
    path('hoodjack_category', views.hoodjack_category, name='hoodjack_category'),
    path('footwear_category', views.footwear_category, name='footwear_category'),
    path('clothe_details/<int:id>/', views.clothe_details, name='clothe_details'),
    path('products/', views.product_list, name='product_list'),
    path('product_details/<int:id>/', views.product_details, name='product_details'),
    path('products2/', views.product_list2, name='product_list2'),
    path('product2_details/<int:id>/', views.product2_details, name='product2_details'),
    path('clothe2_details/<int:id>/', views.clothe2_details, name='clothe2_details'),
    path('add_to_cart/<str:model_type>/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('add_quantity/<int:id>/', views.add_quantity, name='add_quantity'),
    path('delete_quantity/<int:id>/', views.delete_quantity, name='delete_quantity'),
    path('delete_cart/<int:id>/', views.delete_cart, name='delete_cart'),
    path('address', views.address, name='address'),
    path('delete_address/<int:id>/', views.delete_address, name='delete_address'),
    path('checkout', views.checkout, name='checkout'),
    path('save-payment/', views.save_payment, name='save_payment'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('update-order/<int:order_id>/', views.update_order, name='update_order'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('order-success/', views.order_success, name='order_success'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

]
