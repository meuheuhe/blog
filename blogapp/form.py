from django import forms
from .models import Blog
#모델을 기반으로 한

# class BlogPost(forms.ModelForm):
#     class Meta:
#         #블로그 모델을 기반으로한 입력공간으로 만들건데 타이틀과 바디를 공간으로해서 입력공간을 만들것이다.
#         model = Blog
#         fields = ['title', 'body']

class BlogPost(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])