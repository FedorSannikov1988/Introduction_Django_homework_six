from decimal import Decimal
from django.views import View
from datetime import datetime, timedelta
from django.views.generic import TemplateView
from shop.models import Client, Order, Product
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, get_object_or_404
from shop.forms import EditProduct, LoadImageForProduct
from django.core.files.storage import FileSystemStorage


def get_all_customer_orders_and_lists_items_in_order(request,
                                                     name_client: str):
    client = \
        Client.objects.filter(name=name_client).first()

    orders = \
        Order.objects.filter(client=client).all()

    context = {
        "name_client": name_client,
        "orders": orders
    }

    return render(request, "get_all_customer_orders_and_lists_items_in_order.html", context)


def for_sort_products_in_ordered(date_and_time_placing_order: datetime,
                                 what_is_it_compared_to: datetime,
                                 list_products: list,
                                 order: Order):
    if date_and_time_placing_order >= what_is_it_compared_to:
        for one_product in order.product.all():
            if one_product not in list_products:
                list_products.append(one_product)


def get_list_products_ordered_by_customer_from_all_his_orders_v1(request,
                                                                 name_client: str):
    # client = get_object_or_404(Client, name=name_client)
    client = Client.objects.filter(name=name_client).first()

    orders = \
        Order.objects.filter(client=client).all()

    current_datetime = datetime.now()

    seven_days_ago = current_datetime - timedelta(days=7)
    thirty_days_ago = current_datetime - timedelta(days=30)
    # year_days_ago = current_datetime - timedelta(days=365)
    year_days_ago_v2 = current_datetime - relativedelta(years=1)

    seven_days_ago_list_product: list = []
    thirty_days_ago_list_product: list = []
    year_ago_list_product: list = []

    for order in orders:
        date_and_time_placing_order: datetime = \
            order.date_and_time_placing_order.replace(tzinfo=None)

        for_sort_products_in_ordered(list_products=
                                     seven_days_ago_list_product,
                                     date_and_time_placing_order=
                                     date_and_time_placing_order,
                                     what_is_it_compared_to=
                                     seven_days_ago,
                                     order=
                                     order)

        for_sort_products_in_ordered(list_products=
                                     thirty_days_ago_list_product,
                                     date_and_time_placing_order=
                                     date_and_time_placing_order,
                                     what_is_it_compared_to=
                                     thirty_days_ago,
                                     order=
                                     order)

        for_sort_products_in_ordered(list_products=
                                     year_ago_list_product,
                                     date_and_time_placing_order=
                                     date_and_time_placing_order,
                                     what_is_it_compared_to=
                                     year_days_ago_v2,
                                     order=
                                     order)

    context = {
        "name_client": name_client,
        "products": [
            seven_days_ago_list_product,
            thirty_days_ago_list_product,
            year_ago_list_product
        ]
    }

    return render(request,
                  "get_list_products_ordered_by_customer_from_all_his_orders.html",
                  context)


class GetListProductsOrderedByCustomerIdFromAllHisOrdersV2(View):

    def get(self, request, id_client: int):
        client = get_object_or_404(Client, pk=id_client)

        orders = \
            Order.objects.filter(client=client).all()

        current_datetime = datetime.now()

        seven_days_ago = current_datetime - timedelta(days=7)
        thirty_days_ago = current_datetime - timedelta(days=30)
        year_days_ago_v2 = current_datetime - relativedelta(years=1)

        seven_days_ago_list_product: list = []
        thirty_days_ago_list_product: list = []
        year_ago_list_product: list = []

        for order in orders:
            date_and_time_placing_order: datetime = \
                order.date_and_time_placing_order.replace(tzinfo=None)

            for_sort_products_in_ordered(list_products=
                                         seven_days_ago_list_product,
                                         date_and_time_placing_order=
                                         date_and_time_placing_order,
                                         what_is_it_compared_to=
                                         seven_days_ago,
                                         order=
                                         order)

            for_sort_products_in_ordered(list_products=
                                         thirty_days_ago_list_product,
                                         date_and_time_placing_order=
                                         date_and_time_placing_order,
                                         what_is_it_compared_to=
                                         thirty_days_ago,
                                         order=
                                         order)

            for_sort_products_in_ordered(list_products=
                                         year_ago_list_product,
                                         date_and_time_placing_order=
                                         date_and_time_placing_order,
                                         what_is_it_compared_to=
                                         year_days_ago_v2,
                                         order=
                                         order)

        context = {
            "name_client": client.name,
            "products": [
                seven_days_ago_list_product,
                thirty_days_ago_list_product,
                year_ago_list_product
            ]
        }

        return render(request,
                      "get_list_products_ordered_by_customer_from_all_his_orders.html",
                      context)


class GetListProductsOrderedByCustomerIdFromAllHisOrdersV3(TemplateView):
    template_name = "get_list_products_ordered_by_customer_from_all_his_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        id_client = self.kwargs['id_client']

        client = get_object_or_404(Client, pk=id_client)

        orders = \
            Order.objects.filter(client=client).all()

        current_datetime = datetime.now()

        seven_days_ago = current_datetime - timedelta(days=7)
        thirty_days_ago = current_datetime - timedelta(days=30)
        year_days_ago_v2 = current_datetime - relativedelta(years=1)

        seven_days_ago_list_product: list = []
        thirty_days_ago_list_product: list = []
        year_ago_list_product: list = []

        for order in orders:
            date_and_time_placing_order: datetime = \
                order.date_and_time_placing_order.replace(tzinfo=None)

            for_sort_products_in_ordered(list_products=
                                         seven_days_ago_list_product,
                                         date_and_time_placing_order=
                                         date_and_time_placing_order,
                                         what_is_it_compared_to=
                                         seven_days_ago,
                                         order=
                                         order)

            for_sort_products_in_ordered(list_products=
                                         thirty_days_ago_list_product,
                                         date_and_time_placing_order=
                                         date_and_time_placing_order,
                                         what_is_it_compared_to=
                                         thirty_days_ago,
                                         order=
                                         order)

            for_sort_products_in_ordered(list_products=
                                         year_ago_list_product,
                                         date_and_time_placing_order=
                                         date_and_time_placing_order,
                                         what_is_it_compared_to=
                                         year_days_ago_v2,
                                         order=
                                         order)

        context['name_client'] = client.name
        context['products'] = [
            seven_days_ago_list_product,
            thirty_days_ago_list_product,
            year_ago_list_product
        ]
        return context


def page_not_found(request, exception):
    return render(request, 'for_404.html', status=404)


def form_for_edit_product_information(request):

    if request.method == 'POST':

        form_for_edit_product = EditProduct(request.POST)

        if form_for_edit_product.is_valid():

            product = form_for_edit_product.cleaned_data['product']
            name = form_for_edit_product.cleaned_data['name']
            description = form_for_edit_product.cleaned_data['description']
            price = form_for_edit_product.cleaned_data['price']
            quantity = form_for_edit_product.cleaned_data['quantity']

            #product.name = name
            #product.description = description
            #decimal_price: Decimal = Decimal(price)
            #product.price = decimal_price
            #product.quantity = quantity
            #product.save()

            product = Product.objects.get(pk=product.pk)

            if product:
                product.name = name
                product.description = description
                decimal_price: Decimal = Decimal(price)
                product.price = decimal_price
                product.quantity = quantity
                product.save()
    else:
        form_for_edit_product = EditProduct()

    context = {
        "form_for_edit_product": form_for_edit_product,
    }

    return render(request,
                  "form_for_edit_product_information.html",
                  context)


def form_for_load_image_for_product(request):

    if request.method == 'POST':

        form = \
            LoadImageForProduct(request.POST, request.FILES)

        if form.is_valid():

            image_file = request.FILES['image']

            product = form.cleaned_data['product']
            product = Product.objects.get(pk=product.pk)

            if product:
                product.image.save(image_file.name, image_file)
                product.save()

            #image = form.cleaned_data['image']
            #fs = FileSystemStorage()

            #product = form.cleaned_data['product']

            #product = Product.objects.get(pk=product.pk)

            #if product:
            #    upload_to_path = \
            #        product._meta.get_field('image').upload_to
            #    name_image = image.name
            #
            #    fs.save(upload_to_path + name_image, image)
            #    product.image = upload_to_path + name_image
            #    product.save()

    else:
        form = LoadImageForProduct()

    context = {
        "form": form,
    }

    return render(request,
                  'form_for_load_image_for_product.html',
                  context)


class FormForLoadImageForProductV2(View):

    def get(self, request):

        form = LoadImageForProduct()

        context = {
            "form": form
        }
        return render(request,
                      'form_for_load_image_for_product.html',
                      context)

    def post(self, request):

        form = \
            LoadImageForProduct(request.POST, request.FILES)

        if form.is_valid():

            image_file = request.FILES['image']

            product = form.cleaned_data['product']
            product = Product.objects.get(pk=product.pk)

            if product:
                product.image.save(image_file.name, image_file)
                product.save()

        context = {
            "form": form
        }
        return render(request,
                      'form_for_load_image_for_product.html',
                      context)