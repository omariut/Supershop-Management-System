from .models import *
from django import forms
from django.core.exceptions import ValidationError

#Form for order entry
class OrderForm(forms.ModelForm):
    class Meta:
        model=OrderItem
        fields= "__all__"
        exclude=['order']
    # raise validation error if ordered quantity is larger than stock limit
    def clean_quantity(self):
        products=self.cleaned_data.get('products')
        quantity=self.cleaned_data.get('quantity')
        if quantity >  products.stock_quantity :
            raise ValidationError(f'Stock Limit Exceeds!  { products.stock_quantity} units are remaining!' )
        return  quantity
    quantity= models.PositiveIntegerField(default=0, null=True, blank=True, validators=[clean_quantity])
                

#Form for customer data entry
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields= "__all__"
        