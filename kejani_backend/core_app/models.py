from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MinValueValidator
import uuid
from .managers import SoftDeleteManager
from django.utils.text import slugify





class User(AbstractUser):
    """    
Unified user model with role-based access
    """


ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('landlord','Landlord'),
    ('tenant','Tenant'),
)    


role  = models.CharField(max_length=20,choices=ROLE_CHOICES, default=None, null=True)
phone  = models.CharField(max_length=20,unique=True, blank=True, null=True)
is_verified = models.BooleanField(default=False)
created_at = models.DateTimeField(auto_now_add=True)
updated_at =models.DateTimeField(auto_now=True)

approval_status = models.CharField(
    max_length=20,
    choices=(('pending','Pending'),('approved','Approved'),('rejected','Rejected')),
    default='pending',
    db_index=True

)

class Meta:
        ordering = ['-created_at']
    
def __str__(self):
    return f"{self.get_full_name() ({self.role or 'unassigned'})}"



class Landlord(models.Model):
    """
    Extend profile only for landlords
    """

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='landlord_profile')
    id_number = models.CharField(max_length=30,unique=True,blank=True)
    number_of_properties = models.PositiveIntegerField(default=0)
    subscription_tier = models.CharField(
        max_length=20,
        choices=(
            ('starter','Starter'),
            ('growth','Growth'),
            ('professional','Professional'),
            ('enterprise','Enterprise'),
            ('trial','Trial'),
        ),
        default='Trial'
    )
    subscription_expires = models.DateField(null=True,blank=True)
    sms_quota_remaining = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"Landlord:{self.user.get_full_name()}"


class Property(models.Model):
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE,related_name='properties')
    name  = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220,unique=True,blank=True)
    location = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    total_units = models.PositiveIntegerField(default=0)
    is_listed_publily = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.landlord.user.get_full_name()})"





class Unit(models.Model):
    STATUS_CHOICES = (
        ('vacant','Vacant'),
        ('occupied','Occupied'),
        ('maintenance','Under Maintenance'),
        ('reserved','Reserved'),
    )



    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='units')
    unit_number = models.CharField(max_length=50)
    bedrooms = models.PositiveIntegerField(max_length=50)
    rent_amount = models.DecimalField(max_digits=12,decimal_places=3,validators=[MinValueValidator(0)])
    rent_cycle = models.CharField(
        max_length=20,
        choices=('monthly','Monthly',('quarterly','Quarterly'),('yearly','Yearly')),
        default='monthly'
    )

    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='vacant',db_index=True)
    floor = models.PositiveIntegerField(max_length=50,blank=True)
    size_sqft = models.PositiveIntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)










class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models