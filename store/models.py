from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    stock_quantity = models.PositiveIntegerField(default=0,
                                                 null=True,
                                                 blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=13)
    customer_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.customer_name


class Order(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        """Returns the url to access a detail order for this order."""
        return reverse('order-details', args=[str(self.id)])

    @property
    def grand_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def cart_total_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    products = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.products.price*self.quantity
        return total
