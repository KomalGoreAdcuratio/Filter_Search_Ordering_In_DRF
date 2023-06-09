# Generated by Django 4.1.7 on 2023-04-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=25)),
                ('product_name', models.CharField(max_length=25)),
                ('type', models.CharField(choices=[('stationary', 'st'), ('kitchen', 'kit'), ('gardening', 'gr')], default='stationary', max_length=15)),
                ('price_tag', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discout', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]
