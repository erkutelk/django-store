from django.urls import path
from . import views
from .forms import loginform, PasswordResetForm, PasswordChangeForm, MyPasswordResetForm
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home),
    path('home/<str:slug>', views.popiler_detay, name='erkek_popiler'),
    path('register/', views.CustomerRegisterView.as_view(), name='register'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='Home/login.html', authentication_form=loginform), name='login'),
    path('profile/', views.ProfileView.as_view(), name='Profile'),
    path('addres/', views.AddressView.as_view(), name='adres'),
    path('addres/update/<int:pk>/', views.UpdateAddressView.as_view(), name='adres_update'),

    # Şifre Sıfırlama URL'leri
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='Home/pasword_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='Home/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='Home/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name='Home/password_reset_complete.html'), name='password_reset_complete'),

    # Şifre Değiştirme URL'leri
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='Home/changespassword.html', form_class=PasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='Home/passwordchangedone.html'), name='passwordchangedone'),


    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('add-to-cart/',views.add_to_card,name='add-to-card'),
    path('home/add-to-cart/',views.home_add_cart,name='add-to-card-home'),
    path('cart/',views.show_card,name='showcart'),
    path('cart/delete/<int:id>',views.cart_delete,name='cart_delete'),
    path('about',views.about,name='about'),
    # path('sepet/',view=add_to_cart,name='sepet-goster'),
]
