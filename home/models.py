from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL 
import datetime

class StatusPinjam(models.Model):
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.status)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True )
    nama = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(default='images/profile/profil.png' ,null=True, blank=True,upload_to='images/profile/' )
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.nama)
    

class SaldoAwal(models.Model):
    nama = models.ForeignKey(Profile, on_delete=CASCADE, null=True) 
    nominal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    month = models.CharField(max_length=100, null=True, blank=False) 
    
    def __str__(self):
        return str(self.nama)
    
    def save(self, *args, **kwargs):
        nows = datetime.datetime.now()
        mon = nows.strftime("%B-%Y")
        self.month = mon
        super(SaldoAwal, self).save(*args, **kwargs)
        
    # @property
    # def Month(self):
    #     if self.Date:
    #         return self.Date.strftime("%B")
    #     return "No date entry"
        
    
class Pinjaman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True )
    nama = models.CharField(max_length=200, null=True)
    keperluan = models.CharField(max_length=100)
    tanggal = models.DateField(auto_now=True)
    nominal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(StatusPinjam, on_delete=SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return str(self.nama)
    
class Bayar(models.Model):
    nama = models.ForeignKey(Pinjaman, on_delete=models.SET_NULL,null=True)
    tanggal = models.DateField(auto_now=True)
    nominal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nama)
    
class Pengeluaran(models.Model):
    nama = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True )
    nominal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    keperluan = models.CharField(max_length=100)
    tanggal = models.DateField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-tanggal"]

    def __str__(self):
        return str(self.nama)
    
