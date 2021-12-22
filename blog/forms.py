from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        # tells the Django to load this field  as HTML text element
        # attrs = dictionary that allows us to specify  CSS classes and placeholder text  "Your Name"
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )