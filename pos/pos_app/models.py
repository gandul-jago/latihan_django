""" from django.db import models
# Create your models here.

class TableResto(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    table_status = models.IntegerField(default=1)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name """
#yang di atas dijadiin komentar dlu, krn mau jalanin modul 7


#modul 7    
from django.db import models
from django.contrib.auth.models import User

class StatusModel(models.Model):
    status_choices = (
        ('Aktif','Aktif'),
        ('Tidak Aktif', 'Tidak Aktif'),
    )            
    name = models.CharField(max_length = 50, unique = True)
    description = models.TextField(blank = True, null = True)
    status = models.CharField(max_length = 15, 
        choices = status_choices, default = 'Aktif')
    user_create = models.ForeignKey(User, 
        related_name = 'user_create_status_model', 
        blank = True, null = True, on_delete = models.SET_NULL)
    user_update = models.ForeignKey(User, 
        related_name = 'user_update_status_model', 
        blank = True, null = True, on_delete = models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.name)

class Category(models.Model):    
    name = models.CharField(max_length = 100)    
    status = models.ForeignKey(StatusModel, related_name = 'status_category', on_delete = models.PROTECT)    
    user_create = models.ForeignKey(User, related_name = 'user_create_category', 
        blank = True, null = True, on_delete = models.SET_NULL)
    user_update = models.ForeignKey(User, related_name = 'user_update_category', 
        blank = True, null = True, on_delete = models.SET_NULL)
    
    #nanti kalo impor, ini bawah di pagari, supaya g error pas import
    #trus makemigrations, lalu migrate. kalo dah siap import, buka, dan migrate lg

    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class MenuResto(models.Model):    
    status_menu_choices = (
        ('Ada','Ada'),
        ('Habis', 'Habis'),
    )        
    code = models.CharField(max_length = 20, unique = True)
    name = models.CharField(max_length = 100)    
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.CharField(max_length = 200)    
    image_menu = models.ImageField(default = None, upload_to = 'menu_images/', blank = True, null = True)    
    category = models.ForeignKey(Category, related_name = 'category_menu', blank = True, null = True, on_delete = models.SET_NULL)
    menu_status = models.CharField(max_length = 15, choices = status_menu_choices, default = 'Ada')
    status = models.ForeignKey(StatusModel, related_name = 'status_menu', on_delete = models.PROTECT)    
    user_create = models.ForeignKey(User, related_name = 'user_create_menu', blank = True, null = True, on_delete = models.SET_NULL)
    user_update = models.ForeignKey(User, related_name = 'user_update_menu', blank = True, null = True, on_delete = models.SET_NULL)
    
    #nanti kalo impor, ini bawah di pagari, supaya g error pas import
    #trus makemigrations, lalu migrate. kalo dah siap import, buka, dan migrate lg
    #nanti pas makemigrations kalo ada pilihan 1 atau 2, pilih 2
    #nnati kalo ada timezone, enter aja.
    #2x gt keknya

    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']