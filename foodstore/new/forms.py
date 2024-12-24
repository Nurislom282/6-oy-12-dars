from django import forms

from .models import Category, Dish


class PostForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "placeholder": "Ovqat nomi",
        'class': "form-control"
    }))
    discription = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Ovqathaqida",
        'class': "form-control",
        "rows": 3
    }))
    photo = forms.ImageField(required=False, widget=forms.FileInput())
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={
                                          "class": "form-select"}))
    def create(self):
        post = Dish.objects.create(**self.cleaned_data)
        return post


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, error_messages={"error": "Max 150 ta simvol bo'lishi kerak"},
                               widget=forms.TextInput(attrs={
                                   "id": "form3Example1cg",
                                   "class": "form-control form-control-lg"
                               }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "id": "form3Example3cg",
        "class": "form-control form-control-lg"
    }))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        "id": "form3Example4cg",
        "class": "form-control form-control-lg"
    }))
    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        "id": "form3Example4cdg",
        "class": "form-control form-control-lg"
    }))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())