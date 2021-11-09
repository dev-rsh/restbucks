from django.db import models
from django.conf import settings


class Attribute(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'attribute'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    attributes = models.ManyToManyField(Attribute, related_name='attributes', through='ProductAttribute')

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attributes')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='product_attributes')

    class Meta:
        db_table = 'product_attribute'

    def __str__(self):
        return f"{self.product}, {self.attribute}"


class AttributeOptions(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=250)

    class Meta:
        db_table = 'attribute_options'

    def __str__(self):
        return f"{self.attribute}, {self.option}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField('date ordered')
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'order'

    def get_status(self):
        if self.status == 0:
            return 'waiting'
        elif self.status == 1:
            return 'preparing'
        elif self.status == 2:
            return 'ready'
        else:
            return 'delivered'

    def __str__(self):
        return f"{self.user}, {self.order_date}, {self.get_status()}"

    get_status.short_description = 'status'


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_products')
    options = models.JSONField()
    quantity = models.IntegerField()

    class Meta:
        db_table = 'cart'
