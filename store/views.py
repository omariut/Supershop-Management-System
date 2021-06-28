from django.shortcuts import render
from .models import *
from .form import *
from django.views import generic
import segno
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages

# customer data entry
def customer_data_entry(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            instance=Customer()
            instance=form
            instance.save()
            return HttpResponseRedirect('order-entry')
    else:
        form = CustomerForm()
    return render(request, 'store/customer-data-entry.html', {'form': form})

# order entry
def order_entry(request):
    customer=Customer.objects.latest('id')
    order, created =Order.objects.get_or_create(customer=customer)
    products=Product.objects.all()

    if request.method == "POST":
        
        form = OrderForm(request.POST)
        if form.is_valid():
            instance=OrderItem()
            instance.order=order
            instance.products=form.cleaned_data.get('products')
            instance.quantity=form.cleaned_data.get('quantity')
            if instance.quantity <= instance.products.stock_quantity:
                instance.products.stock_quantity -= instance.quantity
                instance.products.save()
                instance.save()
                return HttpResponseRedirect('order-entry')
    else:
        form = OrderForm()
    return render(request, 'store/order.html', {'products':products, 'form': form, 'customer':customer, 'order': order})

# preparing and printing invoice
def invoice(request):
    customer=Customer.objects.latest('id')
    order=Order.objects.get(customer=customer)
    # QR code generation
    qr = segno.make_qr('Name:' + customer.customer_name+ '\n' + 
                        'phone:' + customer.customer_phone + '\n'+
                        'E-mail:' + customer.customer_email)
    qr.save('store/static/qr-code/qr-code.png', scale=7) # saving qr code image 
    return render(request, 'store/invoice.html', {'order':order, 'qr': qr})

#list of all orders
class OrderListView(generic.ListView):
    model=Order
#detail view of orders 
class OrderDetailView(generic.DetailView):
    model=Order
    def order_detail_view(request, primary_key):
        try:
            order = Order.objects.get(pk=primary_key)
        except Order.DoesNotExist:
            raise ('Order does not exist')
    


