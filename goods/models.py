from tabnanny import verbose
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nazwa")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = 'category'
        verbose_name =  "Kategorie"
        verbose_name_plural = "Kategorii"

    def __str__(self):
        return self.name 

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nazwa")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name= "Szczegoly")
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Cena")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Rabat w %")
    quantity = models.PositiveBigIntegerField(default=0, verbose_name="Illosc")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Kategoria")

    class Meta:
        db_table = 'product'
        verbose_name = 'Produkt'
        verbose_name_plural = "Produkty"

    def __str__(self):
        return f'{self.name} Illosc - {self.quantity}'
    
    def display_id(self):
        return f"{self.id:05}"

    def self_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        return self.price
    
