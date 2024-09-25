from django import forms
from .models import Product

class ProductForm(forms.Form): #crea un formulario
    name = forms.CharField(max_length= 200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripción")
    price = forms.DecimalField(max_digits= 10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="Disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)
    stock = forms.IntegerField(max_value=200, label = "Cantidad")
    date = forms.DateField(label="Fecha")

    def save(self): #cuando un usuario usa el formulario y lo guardamos, creamos una instancia de product en la base de datos
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo'],
            stock=self.cleaned_data['stock'],
            date=self.cleaned_data['date'],

        )