from django import forms
from django.db.transaction import commit
from django.forms import widgets
from multiupload.fields import MultiImageField, MultiFileField

from . import models
from .models import Post,Comment
GEEKS_CHOICES =(
    ("PD", "Product"),
    ("PJ", "Projects"),
)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','caption','tag','postDivision']
        widgets = {
            "caption": forms.Textarea(attrs={"rows": 3}),
        }


# class FileSetForm(forms.ModelForm):
#     class Meta:
#         model = FileSet
#         fields = ('fileName',)

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title','caption','tag','postDivision']
#         widgets = {
#             "caption": forms.Textarea(attrs={"rows": 3}),
#         }
#     file_set = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    # def save(self, commit=True):
    #     post = super(PostForm, self).save(commit)
    #     for each in self.cleaned_data['files']:
    #         FileSet.objects.create(file=each, post=post)
    #
    #     return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['message']
        widgets={
            "message" : forms.Textarea(attrs={"rows":3}),
        }