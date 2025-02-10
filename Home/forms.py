from django import forms  # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User  # type: ignore
from .models import Customer

class loginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'zipcode', 'state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
        }

    class MyPasswordChangeForm(PasswordChangeForm):
        old_password = forms.CharField(
            label='Old Password',
            widget=forms.PasswordInput(attrs={'autofous': 'True', 'autocomplete': 'current-password', 'class': 'form-control'})
        )
        new_password1 = forms.CharField(
            label='New Password',
            widget=forms.PasswordInput(attrs={'autofous': 'True', 'autocomplete': 'new-password', 'class': 'form-control'})
        )
        new_password2 = forms.CharField(
            label='Confirm New Password',
            widget=forms.PasswordInput(attrs={'autofous': 'True', 'autocomplete': 'new-password', 'class': 'form-control'})
        )

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView

class MyPasswordChangeView(PasswordChangeView):
    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)  # kullanıcıyı güncelle
        # Burada e-posta gönderimi yapılabilir
        send_mail(
            'Şifre Değişikliği',
            'Şifreniz başarıyla değiştirildi.',
            'your_email@gmail.com',
            [self.request.user.email],
        )
        return super().form_valid(form)
