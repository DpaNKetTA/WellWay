from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(),

            'comment': forms.Textarea(attrs={
                'class': 'input-group', 'placeholder': 'Ваши впечатления', 'rows': 5
            }),
        }