from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Sale

from django.utils import timezone

# Search Function Imports
from django.db.models import Q

# Import Message Framework
from django.contrib import messages

# Forms imports
from .forms import ProductForm, SaleForm

from django.contrib.auth.decorators import login_required


# Generic Views Imports
from django.views.generic import TemplateView, UpdateView, DeleteView, DetailView, CreateView, FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class Dashboard(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'store/dashboard.html'
    context_object_name = 'products'
    login_url = '/auth/login/'
    redirect_field_name = 'next'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'dashboard'
        context['products'] = Product.objects.all()
        context['sales'] = Sale.objects.all()
        return context
    
    



class CreatProduct(FormView):
    template_name = 'store/add_product.html'
    form_class = ProductForm
    success_url = '/store/all-products/'
    context_object_name = 'products'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)
    
class CreateSale(LoginRequiredMixin,FormView):
    template_name = 'store/add_sale.html'
    form_class = SaleForm
    success_url = '/store/all-sales/'
    login_url = '/auth/login/'
    redirect_field_name = 'next'
    context_object_name = 'sales'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'add_sale'
        context['sales'] = Sale.objects.all()
        context['sales_count'] = context['sales'].count()
        return context
    
    def form_valid(self, form):
        form.save(commit=False)
        form.instance.issued_by = self.request.user
        form.save()
        return super().form_valid(form)
    

class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'store/all_products.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'all_products'
        context['model'] = Product.objects.all()
        return context
    
class SaleList(ListView):
    model = Sale
    context_object_name = 'sales'
    template_name = 'store/all_sales.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'all_sales'
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'store/view_product.html'
    context_object_name = 'product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'product_detail'
        context['product_cat'] = context['product'].category.all()
        context['product_cat_count'] = context['product_cat'].count()
        return context



class SaleDetail(DetailView):
    model = Sale
    template_name = 'store/view_sale.html'
    context_object_name = 'sale'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'sale_detail'
        return context


class DeleteSale(DeleteView):
    model = Sale
    template_name = "store/delete.html"
    context_object_name = 'obj'
    success_url = '/store/all-sales/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'delete_sale'
        return context

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'store/delete.html'
    context_object_name = 'obj'
    success_url = '/store/all-products/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'delete_product' 
        return context

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'store/add_product.html'
    success_url = '/store/all-products/'
    form_class = ProductForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'update_product'
        context['created_by'] = Product.objects.all()
        return context
    
    def get(self):
        get_object_or_404(Product, pk=1)
            
    

class UpdateSale(UpdateView):
    model = Sale
    template_name = 'store/add_sale.html'
    success_url = '/store/all-sales/'
    form_class = SaleForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'update_sale'
        return context
    


def search_func(request):
    query = request.GET.get('query') if request.GET.get('query') != None else ''
    
    sales = Sale.objects.filter(
        Q(product__name__icontains=query) |
        Q(address__icontains=query) |
        Q(issued_by__username__icontains=query)
    )
    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(created_by__username__icontains=query)
    )
    sales_count = sales.count()
    products_count = products.count()
    
    context = {
        'sales':sales,
        'products':products,
        'sales_count':sales_count,
        'products_count':products_count,
        'query':query,
    }
    return render(request, 'store/search.html', context)