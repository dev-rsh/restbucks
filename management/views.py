from django.shortcuts import render
from django.views import generic

from .models import Product, Attribute, AttributeOptions


class IndexView(generic.ListView):
    template_name = 'management/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


class DetailView(generic.DetailView):
    model = Product
    template_name = 'management/details.html'
