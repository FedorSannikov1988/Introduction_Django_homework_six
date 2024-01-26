from django.contrib import admin
from shop.models import Product, Client,  Order


class ClientAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'address', 'phone_number', 'date_and_time_registration']
    ordering = ['date_and_time_registration']
    list_filter = ['date_and_time_registration']
    search_fields = ['name']
    search_help_text = 'Поиск по полю NAME'

    #fields = ['name', 'email', 'address', 'phone_number', 'date_and_time_registration']
    readonly_fields = ['date_and_time_registration']
    fieldsets = [
        (
            'Имя',
            {
                'description': 'Имя Клиента',
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Электронная почта',
            {
                'description': 'Электронная Почта Клиента',
                'classes': ['wide'],
                'fields': ['email'],
            },
        ),
        (
            'Номер телефона',
            {
                'description': 'Номер Телефона Клиента',
                'classes': ['wide'],
                'fields': ['phone_number'],
            },
        ),
        (
            'Адрес клиента',
            {
                'description': 'Адрес Клиента',
                'classes': ['collapse'],
                'fields': ['address'],
            },
        ),
        (
            'Дата и время регистрации',
            {
                'description': 'Дата и Время Регистрации Клиента - Сделано Не Изменяемым',
                'classes': ['wide'],
                'fields': ['date_and_time_registration'],
            },
        ),
    ]


@admin.action(description="Цену выставить в ноль")
def reset_price(modeladmin, request, queryset):
    queryset.update(price=0)


@admin.action(description="Цену выставить в 1 рубль")
def reset_to_do_1_ruble(modeladmin, request, queryset):
    queryset.update(price=1.0)


@admin.action(description="Количество выставить в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'price', 'quantity', 'about_image', 'date_and_time_additions_product']
    ordering = ['date_and_time_additions_product', 'price', 'quantity']
    list_filter = ['date_and_time_additions_product', 'price', 'quantity']
    search_fields = ['name']
    search_help_text = 'Поиск по полю NAME'
    actions = [reset_price, reset_to_do_1_ruble, reset_quantity]

    #fields = [
    #    ('name', 'price', 'quantity'),
    #    'description',
    #    'date_and_time_additions_product',
    #    'image'
    #]
    readonly_fields = ['date_and_time_additions_product']
    fieldsets = [
        (
            'Название',
            {
                'description': 'Название Продукта',
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Описание',
            {
                'description': 'Описание Продукта',
                'classes': ['collapse'],
                'fields': ['description'],
            },
        ),
        (
            'Цена',
            {
                'description': 'Цена Продукта',
                'classes': ['wide'],
                'fields': ['price'],
            },
        ),
        (
            'Количество',
            {
                'description': 'Количество Продукта',
                'classes': ['wide'],
                'fields': ['quantity'],
            },
        ),
        (
            'Дата и время добавления продукта',
            {
                'description': 'Дата и Время Добавления Продукта',
                'classes': ['wide'],
                'fields': ['date_and_time_additions_product'],
            },
        ),
        (
            'Картинка',
            {
                'description': 'Картинка для товара',
                'classes': ['wide'],
                'fields': ['image'],
            },
        ),
    ]

    def about_image(self, obj):
        if obj.image:
            return 'YES picture'
        else:
            return 'NO picture'


@admin.action(description="Стоимость выставить в ноль")
def reset_total_amount_order(modeladmin, request, queryset):
    queryset.update(total_amount_order=0)


class OrderAdmin(admin.ModelAdmin):

    list_display = ['get_client_name', 'total_amount_order', 'date_and_time_placing_order']
    ordering = ['-date_and_time_placing_order']
    list_filter = ['date_and_time_placing_order', 'total_amount_order']
    search_fields = ['client__name', 'client__email', 'client__phone_number', 'client__address']
    search_help_text = 'Поиск по полю NAME, EMAIL, PHONE_NIMBER, ADDRESS в модели CLIENT'
    actions = [reset_total_amount_order]

    def get_client_name(self, obj):
        return obj.client.name

    #fields = ['client', 'product', 'total_amount_order', 'date_and_time_placing_order']
    readonly_fields = ['date_and_time_placing_order']
    fieldsets = [
        (
            'Клиент',
            {
                'description': 'Клиент Который Сделал Заказ',
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Продукты',
            {
                'description': 'Продукты В Заказе',
                'classes': ['wide'],
                'fields': ['product'],
            },
        ),
        (
            'Стоимость',
            {
                'description': 'Стоимость Всего Заказа',
                'classes': ['wide'],
                'fields': ['total_amount_order'],
            },
        ),
        (
            'Дата и время',
            {
                'description': 'Дата и Время Формирования Заказа',
                'classes': ['wide'],
                'fields': ['date_and_time_placing_order'],
            },
        ),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
