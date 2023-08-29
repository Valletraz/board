from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'message',
            'author',
            'category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("message")
        if description is not None and len(description) < 5:
            raise ValidationError({
                "description": "Новость не может быть менее 5 символов."
            })
        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["title"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name
