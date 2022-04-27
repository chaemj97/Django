from dataclasses import field
from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'test1 form-control',
                'placeholder':'여기에 제목을 입력하세요.',
                'maxlength':10,
            }
        ),
        error_messages={
            'required':'제목을 입력하세요!'
        }
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'test2 form-control',
                'placeholder':'여기에 내용을 작성하세요.',
                'cols':30,
                'rows':10,
            }
        ),
        error_messages={
            'required':'내용을 입력하세요!'
        }
    )

    class Meta:
        model = Article
        # fields = ('title','content')
        fields = '__all__'
        # exclude = ('title')