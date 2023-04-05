from django.db import models

# Create your models here.
#  search wrt cust_name ,product_name, type ,
class  Order(models.Model):
    type_choice=[
        ('stationary','st'),
        ('kitchen','kit'),
        ('gardening','gr')
    ]
    id = models.IntegerField(primary_key=True)
    cust_name=models.CharField(max_length=25)
    product_name=models.CharField(max_length=25)
    type=models.CharField(max_length=15,
                          choices=type_choice,
                          default='stationary')
    price_tag=models.DecimalField( max_digits=5, decimal_places=2)
    discout=models.DecimalField(max_digits=4,decimal_places=2)

    #final_amount=models.DecimalField(default=(price_tag*(100-discout)/100),read_only=True)

    
    class Meta:
        pass