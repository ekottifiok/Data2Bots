from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

PAYMENT_CHOICES = [
    ('none', 'none'),
    ('card', 'card'),
    ('cash', 'cash'),
    ('transfer', 'transfer'),
    ('crypto wallet', 'crypto_wallet')
]

# Create your models here.

class Person(AbstractBaseUser):
    email = models.EmailField(_("email address"), blank=False, unique=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    about = models.TextField()
    title = models.CharField(max_length=25)
    images = models.ImageField(upload_to='product_images')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    

class OrderHistory(models.Model):
    time_stamp = models.DateTimeField(_("time stamp"), default=timezone.now)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT)
    delivered = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=250, blank=True)
    payment_method = models.CharField(choices=PAYMENT_CHOICES, max_length=13, default='None')
    
    def __str__(self):
        return f"{self.person_id} {str(self.time_stamp)}"
    
    class Meta:
        verbose_name_plural = _("Order History")