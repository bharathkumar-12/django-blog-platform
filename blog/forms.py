from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-slate-200 px-4 py-2'}),
            'body': forms.Textarea(attrs={'class': 'w-full rounded-lg border border-slate-200 px-4 py-2', 'rows': 10}),
            'tags': forms.SelectMultiple(attrs={'class': 'w-full rounded-lg border border-slate-200 px-3 py-2'}),
        }


class PostUpdateForm(PostForm):
    pass
