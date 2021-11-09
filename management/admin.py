from django.contrib import admin
from django import forms

from .models import Product, Attribute, AttributeOptions, Order, ProductAttribute


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class AttributeOptionsAdmin(admin.ModelAdmin):
    list_display = ['attribute', 'option']


class OrderAdminForm(forms.ModelForm):
    CHOICES = [(0, 'waiting'), (1, 'preparing'), (2, 'ready'), (3, 'delivered')]
    status = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Order
        fields = '__all__'


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    readonly_fields = ['user', 'order_date']
    list_display = ("user", "order_date", "get_status")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        else:
            return list()


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['product', 'attribute']


admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute)
admin.site.register(AttributeOptions, AttributeOptionsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
