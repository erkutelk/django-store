# myapp/context_processors.py

from .models import Konum,logo,Prodact_categories,home_prodact_kategorileri

def konum_processor(request):
    konum_objects = Konum.objects.all()  
    return {
        'konum': konum_objects 
    }
# Veritabanından bir veriyi çekerken bu verinin bütün sayfalarda gözükmesini istiyoruz bunu şu şekilde yapabiliriz. Bir adet 'context_processors.py Dosyası açarız ve setting kısmında 'verileri girdiğimizde footer ve nav kısımları dinamik olarak güncellenir. veritabanından verileri çekiyorsak bunu kullanmamaız mantıklı.
def logo_processor(request):
    logo_object = logo.objects.first()  
    return {
        'logo': logo_object
    }

def menu_processor(request):
    menu_object=home_prodact_kategorileri.objects.all()
    return{
        'kategori':menu_object
    }