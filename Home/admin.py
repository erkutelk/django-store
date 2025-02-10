from django.contrib import admin
from .models import Customer, Cart, Prodact, ProductImage,logo,Konum,home_prodact_kategorileri,about_page,sirketler,intro_picture
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0  # Resim yüklerken kaç adet resim yükle inputu olacağını belirler
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']


@admin.register(Prodact)
class urunler(admin.ModelAdmin):
    list_display = ['prodact_name', 'price', 'description', 'technical_specifications', 'isActive', 'prodact_categories']  
    inlines = [ProductImageInline]
    #Ürün resimlerini admin sayfasında göstermek için burayı kullanırız.


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'Prodact', 'quantity'] 


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']

@admin.register(logo)
class logo_admin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Konum)
class konum(admin.ModelAdmin):
    list_display = ['konum','mail','telefon']


@admin.register(home_prodact_kategorileri)
class ürünler_home_kategori(admin.ModelAdmin):
    list_display = ['Title','aciklama','isActive']
    filter_horizontal = ['urunler'] 


@admin.register(about_page)
class about_page_edit(admin.ModelAdmin):
    list_display = ['title','aciklama','image']

@admin.register(sirketler)
class about_page2(admin.ModelAdmin):
    list_display = ['title','images','description']


@admin.register(intro_picture)
class about_page3(admin.ModelAdmin):
    list_display = ['title','images','description']

