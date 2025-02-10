from django.db import models # type: ignore
from ckeditor.fields import RichTextField # type: ignore
from django.utils.text import slugify # type: ignore
from django.contrib.auth.models import User # type: ignore

class Prodact_categories(models.Model):  
    categori_name = models.CharField(max_length=12)
    slug = models.SlugField(unique=True, blank=True, null=False, db_index=True)
    isActive = models.BooleanField()
    def __str__(self) -> str:
        return self.categori_name

class Prodact(models.Model):
    prodact_name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    technical_specifications = models.TextField(max_length=150)
    isActive = models.BooleanField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=False, db_index=True)
    prodact_categories = models.ForeignKey(Prodact_categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',default='')# Burada images dediğimiz kısım şu şekilde ilerliyor resimleri bir veritabanı üzerinden tutmak mantıksız  bunu bölmemiz gerekli, bir adet Prodacr images açıyoruz bu bize birden fazla resim eklememize olanak tanıyor.böylelikle ürünlerin id değeri ile prodacimage id değeri aynı olduğunda birden fazla resim eklemiş oluyorz.
    # peki birden fazla resim eklerken admin sayfasındaki görüntü nasıl olucak bunuda 

    # class urunler(admin.ModelAdmin):
    # list_display = ['prodact_name', 'price', 'description', 'technical_specifications', 'isActive', 'prodact_categories', 'image']  
    # inlines = [ProductImageInline]
    
    def __str__(self):
        return self.prodact_name


class ProductImage(models.Model):
    product = models.ForeignKey(Prodact, on_delete=models.CASCADE, related_name='images')  
    image = models.ImageField(upload_to='images/')  

    def __str__(self):
        return f"Image for {self.product.prodact_name}" 


STATE_CHOICES=(('İstanbul','İstanbul'),
               ('İzmir','izmir'),
               ('Çorum','Çorum'))


class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField()
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Prodact=models.ForeignKey(Prodact,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    date=models.DateField(auto_now=True)
    @property
    def total(self):
        return self.quantity * self.Prodact.price
    

class UploadModel(models.Model):
    image=models.ImageField(upload_to='images')

class aciklama(models.Model):
    title=models.TextField()
    description=models.TextField()
    image1_title=models.TextField()
    image2_title=models.TextField()

class logo(models.Model):
    image=models.ImageField(upload_to='images')

class social_Media_images(models.Model):
    title=models.CharField(max_length=15)
    images=models.ImageField(upload_to='images')
    link=models.TextField(max_length=50)

class Konum(models.Model):
    konum=models.TextField(max_length=50)
    mail=models.TextField(max_length=15)
    telefon=models.TextField(max_length=11)


class home_prodact_kategorileri(models.Model):
    Title=models.TextField(max_length=20)
    aciklama=models.TextField(max_length=50)
    urunler=models.ManyToManyField(Prodact)
    isActive=models.BooleanField()

    def __str__(self) -> str:
        return self.Title
    

class intro_picture(models.Model):
    images=models.ImageField(upload_to='images')
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=20)

class about_page(models.Model):
    title=models.TextField(max_length=20)
    aciklama=models.TextField()
    image=models.ImageField(upload_to='images')

class sirketler(models.Model):
    images=models.ImageField(upload_to='images')
    title=models.TextField(max_length=20)
    description=models.TextField(max_length=12)
