from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    # PostForm 자체에 대한 설명이 class Meta.
    class Meta:
        model = Post
        fields = '__all__'
        # 아니면 프로퍼티 몇개만 선택도 가능.
