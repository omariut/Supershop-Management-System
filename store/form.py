from .models import *
from django import forms
from django.core.exceptions import ValidationError


# Form for order entry
class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"
        exclude = ['order']

    # raise validation error if ordered quantity is larger than stock limit
    def clean_ordered_quantity_validation(self):
        ordered_product = self.cleaned_data.get('products')
        ordered_quantity = self.cleaned_data.get('quantity')
        if ordered_quantity > ordered_product.stock_quantity:
            raise ValidationError(
                f'Stock Limit Exceeds!{ ordered_product.stock_quantity} units are remaining!'
                )
        return ordered_quantity
    quantity = models.PositiveIntegerField(default=0,
                                           null=True,
                                           blank=True,
                                           validators=[clean_ordered_quantity_validation])


# Form for customer data entry
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
