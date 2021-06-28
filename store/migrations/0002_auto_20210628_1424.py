# Generated by Django 3.2.4 on 2021-06-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='catagory',
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
