# Generated by Django 4.2.7 on 2023-12-26 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecomapp', '0017_alter_billing_house_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='trackorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderStuts', models.TextField()),
                ('orderStutsDate', models.DateTimeField(auto_now_add=True)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecomapp.billing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
