from django import forms
from django.forms import ModelForm

from .models import Product, Sale


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['created_by']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name...'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'cols':'2', 'rows':'2', 'placeholder':'Product Description...'}),
            'price':forms.TextInput(attrs={'class':'form-control','type':'number', 'placeholder':'Product Price...'}),
            'quantity':forms.TextInput(attrs={'class':'form-control','type':'number', 'placeholder':'Product Quantity...'}),
            'category':forms.SelectMultiple(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Status...'}),
            'manufacturing_date':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'expiry_date':forms.TextInput(attrs={'class':'form-control','type':'date'}),
        }
        
class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = "__all__"
        exclude = ['issued_by']
        widgets = {
            'product':forms.Select(attrs={'class':'form-control'}),
            'quantity':forms.TextInput(attrs={'class':'form-control','type':'number', 'placeholder':'Product Quantity...'}),
        }