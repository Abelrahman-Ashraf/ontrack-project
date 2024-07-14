from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.core.validators import RegexValidator

#from django.utils.translation import ugettext_lazy as _
# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User , verbose_name=("user"), on_delete=models.CASCADE)
    name=models.CharField(("name"), max_length=50 ,default="client")
    email=models.EmailField(("email"), max_length=254)
    location=models.TextField(("location"))
    phone=models.CharField(("phone"), max_length=15)
    slug=models.SlugField(("slug"),blank=True,null=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        
        super(profile, self).save(*args, **kwargs)



    class Meta:
        verbose_name = ("profile")
        verbose_name_plural = ("profiles")

    def __str__(self):
        return '%s' %(self.user.username)
    

def create_profile(sender , **kwargs):
    if kwargs['created']:
        profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile , sender=User)



# model of shipments
    
class Shipment(models.Model):
    sent_by = models.ForeignKey(User,verbose_name=("user"), on_delete=models.CASCADE)
    shipment_id = models.AutoField(primary_key=True,validators=[RegexValidator(r'^\d+$', 'Only numbers are allowed')])
    shipment_type = models.CharField(verbose_name=("type"),max_length=100)
    shipment_weight = models.DecimalField(verbose_name=("wieght"),max_digits=10, decimal_places=2)
    receiver_name = models.CharField(verbose_name=("receiver name"),max_length=200)
    sender_name = models.CharField(verbose_name=("sender name"),max_length=200)
    sender_phone = models.CharField(verbose_name=("sender phone"),max_length=20)
    receiver_phone = models.CharField(verbose_name=("reciever phone"),max_length=20)
    start_location = models.CharField(verbose_name=("start location"),max_length=200)
    last_location = models.CharField(verbose_name=("last location"),max_length=200)
    received_date = models.DateField(verbose_name=("resieved date"),null=True, blank=True)
    about_shipment = models.TextField(verbose_name=("about"),blank=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')


    class Meta:
        verbose_name = ("shipment")
        verbose_name_plural = ("shipments")

    def __str__(self):
        return f"Shipment {self.shipment_id} - {self.sent_by} - {self.shipment_type}"    


