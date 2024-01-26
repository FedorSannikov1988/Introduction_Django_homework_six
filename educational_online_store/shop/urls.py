from django.urls import path
from .views import get_all_customer_orders_and_lists_items_in_order, \
                   get_list_products_ordered_by_customer_from_all_his_orders_v1, \
                   GetListProductsOrderedByCustomerIdFromAllHisOrdersV2, \
                   GetListProductsOrderedByCustomerIdFromAllHisOrdersV3, \
                   form_for_edit_product_information, \
                   form_for_load_image_for_product, \
                   FormForLoadImageForProductV2


urlpatterns = [

    path('get_all_customer_orders_and_lists_items_in_order/<str:name_client>/',
         get_all_customer_orders_and_lists_items_in_order,
         name='get_all_customer_orders_and_lists_items_in_order'),

    path('get_list_products_ordered_by_customer_from_all_his_orders/<str:name_client>/',
         get_list_products_ordered_by_customer_from_all_his_orders_v1,
         name='get_list_products_ordered_by_customer_from_all_his_orders'),

    #только для того что бы поработать с классами вариант №2:
    path('get_list_products_ordered_by_customer_from_all_his_orders_v2/<int:id_client>/',
         GetListProductsOrderedByCustomerIdFromAllHisOrdersV2.as_view(),
         name='get_list_products_ordered_by_customer_from_all_his_orders_v2'),

    #только для того что бы поработать с классами вариант №3:
    path('get_list_products_ordered_by_customer_from_all_his_orders_v3/<int:id_client>/',
         GetListProductsOrderedByCustomerIdFromAllHisOrdersV3.as_view(),
         name='get_list_products_ordered_by_customer_from_all_his_orders_v3'),

    path('form_for_edit_product_information/',
         form_for_edit_product_information,
         name='form_for_edit_product_information'),

    path('form_for_load_image_for_product/',
         form_for_load_image_for_product,
         name='form_for_load_image_for_product'),

    #только для того что бы поработать с классами вариант №2:
    path('form_for_load_image_for_product_v2/',
         FormForLoadImageForProductV2.as_view(),
         name='form_for_load_image_for_product_v2'),

]
