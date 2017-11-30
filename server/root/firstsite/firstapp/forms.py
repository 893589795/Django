from django import forms
from django.core.exceptions import ValidationError


def words_validator(comment):
    if len(comment) < 4:
        raise ValidationError('Not enough words')


class CommentForm(forms.Form):
    name = forms.CharField()
    content = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
           'requied': 'please write something'
        },
        validators=[words_validator]

    )
