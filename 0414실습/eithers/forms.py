from django import forms
from .models import Vote,Comment

class VoteForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    issue_a = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    issue_b = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    class Meta:
        model = Vote
        fields = '__all__'

color_choice = [
    ('Blue','Blue'),
    ('Red','Red')
]
class CommentForm(forms.ModelForm):
    pick = forms.ChoiceField(
        choices=color_choice,
        widget=forms.Select(
            attrs={
                'class':'form-select',
            }
        )
    )
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Content'
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('pick','content',)