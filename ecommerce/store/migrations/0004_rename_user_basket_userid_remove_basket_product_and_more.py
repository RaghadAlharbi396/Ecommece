# Generated by Django 4.2.6 on 2023-11-12 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_product_discount_product_discountcategory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='user',
            new_name='userid',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='product',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='size',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='total',
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('size', models.CharField(default='notyet', max_length=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
