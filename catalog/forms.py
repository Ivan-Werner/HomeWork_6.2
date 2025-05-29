from django.forms import ModelForm, BooleanField
from catalog.models import Product, Category
from django.core.exceptions import ValidationError

banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'



class ProductForm(StyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"



    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })
        self.fields['in_active'].widget.attrs.update({
            'class': 'custom-checkbox'
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(word in name.lower() for word in banned_words):
            raise ValidationError("Название не должно содержать запрещенные слова")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if any(word in description.lower() for word in banned_words):
            raise ValidationError("Описание товара не должно содержать запрещенные слова")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def cleaned_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Файл слишком большой")
            if not (image.name.endswitch('.jpg') or image.name.endswitch('.jpeg') or image.name.endswitch('.png')):
                raise  ValidationError("Неверный формат файла")
            return image


class CategoryForm(StyleMixin, ModelForm):
    class Meta:
        model = Category
        fields = "__all__"







