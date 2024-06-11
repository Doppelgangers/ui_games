from django import forms

from ..models import Room


class CreateRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'is_open',)
        widgets = {
            'name': forms.TextInput(),
            'is_open': forms.CheckboxInput(),
        }
        labels = dict(
            name='Название комнаты',
            is_open='Откытая',
        )
