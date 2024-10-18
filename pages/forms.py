from django import forms
from .models import Review, Review2, Review3, Review4, Review5

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

class ReviewForm2(forms.ModelForm):
    class Meta:
        model = Review2
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(),

            'comment': forms.Textarea(attrs={
                'class': 'input-group', 'placeholder': 'Ваши впечатления', 'rows': 5
            }),
        }

class ReviewForm3(forms.ModelForm):
    class Meta:
        model = Review3
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(),

            'comment': forms.Textarea(attrs={
                'class': 'input-group', 'placeholder': 'Ваши впечатления', 'rows': 5
            }),
        }

class ReviewForm4(forms.ModelForm):
    class Meta:
        model = Review4
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(),

            'comment': forms.Textarea(attrs={
                'class': 'input-group', 'placeholder': 'Ваши впечатления', 'rows': 5
            }),
        }

class ReviewForm5(forms.ModelForm):
    class Meta:
        model = Review5
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(),

            'comment': forms.Textarea(attrs={
                'class': 'input-group', 'placeholder': 'Ваши впечатления', 'rows': 5
            }),
        }

