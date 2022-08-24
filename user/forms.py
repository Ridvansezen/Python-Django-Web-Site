from django import forms
from django.contrib.auth.models import User

# Login Formu

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı adı : ")
    password = forms.CharField(label = "Parola : ",widget = forms.PasswordInput)



# Kullanıcı Kayıt formu

class RegisterForm(forms.Form):
     
     username = forms.CharField(max_length = 20, label = "Kullanıcı adı")
     password = forms.CharField(max_length = 20, label = "Parola", widget = forms.PasswordInput)     
     confirm = forms.CharField(max_length = 20, label = "Parolayı doğrulayınız", widget = forms.PasswordInput)     

     def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        checkusers = User.objects.all()
        for a in checkusers:
            if str(a) == username:
                raise forms.ValidationError("Kullanıcı Adı Sistemde Kayıtlı!")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar uyuşmuyor !")

        values = {
            "username" : username,
            "password" : password
        }
        return values

