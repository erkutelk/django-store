from django.shortcuts import render, get_object_or_404,redirect # type: ignore
from .models import Prodact, Customer,Cart,aciklama,logo,social_Media_images,Konum,home_prodact_kategorileri,intro_picture,sirketler,about_page,Prodact_categories
from .forms import CustomerRegistrationForm, loginform, CustomerProfileForm
from django.views import View # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.utils.decorators import method_decorator # type: ignore

def about(request):
    partials=intro_picture.objects.all()
    partials2=about_page.objects.all()
    partials3=sirketler.objects.all()
    return render(request,'Home/about.html',{'intro_about':partials,
                                             'partials':partials2,
                                             'partials3':partials3})

def home(request):
    urun_kategorileri=Prodact_categories.objects.all()
    prodact_item_object_erkek = Prodact.objects.all()
    aciklama_objects=aciklama.objects.all()
    konum_objects=Konum.objects.all()
    social_Media_images_object=social_Media_images.objects.all()
    ürünler_kategori_card_object=home_prodact_kategorileri.objects.all()
    return render(request, 'Home/home.html', {
        'erkek': prodact_item_object_erkek,
        'aciklama':aciklama_objects,
        'social_media':social_Media_images_object,
        'konum':konum_objects,
        'katogiler_models_card':ürünler_kategori_card_object,
        'ürünKategori':urun_kategorileri
    })

def popiler_detay(request, slug):
    isim = get_object_or_404(Prodact, slug=slug)
    return render(request, 'Home/single-product.html',{'isim': isim})

class CustomerRegisterView(View):
    #Kullanıcının siteye girdiği zaman formu görmesini sağlayan fonksiyon.
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'Home/register.html', {'form': form})
    
    #Sitede kullanıcının formu veritabanına göndermesini sağlayan fonksiyon bu şekilde
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başarılı bir şekilde kayıt yapıldı...')
        else:
            messages.error(request, 'Hata meydana geldi, lütfen tekrar deneyin.')
        return render(request, 'Home/register.html', {'form': form})
    

#Giriş yapmadan gözükmesini istemedeiğim için bu fonksiyon gerekli.
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'Home/profile.html', {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profil güncellendi.')
        else:
            messages.error(request, 'Bir hata meydana geldi. Lütfen tekrar deneyin.')
        return render(request, 'Home/profile.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        add = Customer.objects.filter(user=request.user)
        return render(request, 'Home/addres.html', {'naber': add})

@method_decorator(login_required, name='dispatch')
class UpdateAddressView(View):
    def get(self, request, pk):
        add = get_object_or_404(Customer, pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'Home/adres_update.html', {'form': form})

    def post(self, request, pk):
        add = get_object_or_404(Customer, pk=pk)
        form = CustomerProfileForm(request.POST, instance=add)
        if form.is_valid():
            form.save()
            messages.success(request, 'Adres güncellendi.')
        else:
            messages.error(request, 'Bir hata meydana geldi. Lütfen tekrar deneyin.')
        return render(request, 'Home/adres_update.html', {'form': form})


def add_to_card(request):
    try:
        user=request.user
        prodact_id=request.GET.get('prod_id')
        quantity=request.GET.get('quantity')
        prodact=Prodact.objects.get(pk=prodact_id)
        Cart(user=user,Prodact=prodact,quantity=quantity).save()
        return redirect('/cart')
    except:
        return render(request,'Home/giriş_yapiniz.html')

def home_add_cart(request):
    user=request.user
    prodact_id=request.GET.get('prod_id')
    quantity=request.GET.get('quantity')
    prodact=Prodact.objects.get(pk=prodact_id)
    Cart(user=user,Prodact=prodact,quantity=1).save()
    return redirect('/cart')

def show_card(request):
    try:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.Prodact.price
            amount += value

        totalAmount = amount
        return render(request, 'Home/addtocart.html', locals())
    except:
        return render(request,'Home/giriş_yapiniz.html')

def cart_delete(request, id):
    user = request.user
    cart_delete = get_object_or_404(Cart, pk=id, user_id=user)
    if request.method == 'POST':
        cart_delete.delete()
        return redirect('showcart')  # Sepet sayfasına yönlendirme yapın
    return redirect('showcart')  # GET isteği için de aynı sayfaya yönlendirme yapın
