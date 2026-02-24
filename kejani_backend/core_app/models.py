from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone



class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None,**extra_fields):
        extra_fields.setdefault("is_active",1)
        return   self.create_user(username,email,password,**extra_fields)




class User(AbstractBaseUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    password_hash = models.CharField(max_length=255)
    is_active = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELD = ["email"]


    def __str__ (self):
        return self.username

    @property
    def is_landlord(self):
        return self.user_roles.filter(role__role__name="landlord").exists()
    @property
    def is_property_manager(self):
        return self.user_roles.filter(role__role__name="property_manager").exists()

    @property
    def is_tenant(self):
        return self.user_roles.filter(role__role__name="tenant").exists()


    class Role(models.Model):
        role_name = models.CharField(max_length=50,unique=True)
        description = models.TextField(blank=True)
        created_at = models.DateTimeField(default=timezone.now)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.role_name



class  UserRole(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_roles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    asssigned_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("user","role"),
        verbose_name = "User Role"
        verbose_name_plural = "User Roles"




class landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="landlord_profile")
    id_number = models.CharField(max_length=50,unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Landlord: {self.username}"




class PropertyManager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="tenant_profile")
    unit = models.ForeignKey("properties.Unit",on_delete=models.SET_NULL,null=True, related_name="current_tenant")
    emergency_contact = models.DateField(null=True,blank=True)
    lease_start = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)



class Tenant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="tenant_profile")
    unit = models.ForeignKey("properties.Unit",on_delete=models.SET_NULL, null=True, related_name="current_tenant")
    emergency_contact = models.CharField(max_length=100,blank=True)
    lease_start = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Tenant:{self.user.username}"

        




