from django.db import models
from users.models import User
import uuid
from location_field.models.plain import PlainLocationField

class Zones(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=225)
    
    class Meta:
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'

    def __str__(self):
        return self.title
    

class UserDetails(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='users/profile/', blank=True, null=True)
    address = models.TextField()
    home_zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
    location = PlainLocationField(based_fields=['city'], zoom=7, blank=True, null=True)

    class Meta:
        verbose_name = 'UserDetail'
        verbose_name_plural = 'UserDetails'

    def __str__(self):
        return self.user.user_name

class Roles(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=225)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
    
    def __str__(self):
        return self.title

class Ministries(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=225)
    roles = models.ManyToManyField(Roles, blank=True)

    class Meta:
        verbose_name = 'Ministry'
        verbose_name_plural = 'Ministries'

    def __str__(self):
        return self.title

class UserMinistry(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ministry = models.ForeignKey(Ministries, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'UserMinistry'
        verbose_name_plural = 'UserMinistries'
    
    def __str__(self):
        return f'{self.user.user_name} | {self.ministry} | {self.role}'