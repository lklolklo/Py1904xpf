from django import forms
from .models import PollsUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = PollsUser
        fields = ["username","password"]
        widgets = {
            "username": forms.TextInput(
                attrs={"id": "username", "class": "no-round-input", "placeholder": "输入用户名"}),
            "password": forms.PasswordInput(
                attrs={"id": "password", "class": "no-round-input", "placeholder": "输入密码"}),
        }
        help_texts = {
            "username":"",
        }

class RegistForm(forms.ModelForm):
    repeatpassword = forms.CharField(label="重复密码",required=True,widget=forms.PasswordInput(attrs={"class":"no-round-input","id":"registpassword2", "placeholder":"再次输入密码"}))
    class Meta:
        model = PollsUser
        fields = ["username","password","telephone","email"]
        widgets = {
            "username":forms.TextInput(attrs={"id":"registusername","placeholder":"输入用户名","class":"no-round-input" }),
            "password":forms.PasswordInput(attrs={"class":"no-round-input","id":"registpassword", "placeholder":"输入密码"}),
            "telephone": forms.TextInput(
                attrs={"class": "no-round-input", "id": "telephone", "placeholder": "输入手机号"}),
            # "repeatpassword":forms.PasswordInput(attrs={"class":"no-round-input","id":"registpassword2", "placeholder":"重复密码"}),
            "email":forms.EmailInput(attrs={"class": "no-round-input", "id": "email", "placeholder": "输入邮箱"})
        }
        help_texts = {
            "username":"",
        }
        labels = {
            "telephone":"手机号"
        }
