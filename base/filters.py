from django_filters import CharFilter, FilterSet, MultipleChoiceFilter

from django import forms

from .models import *

CHOICES = (
    ('job', 'job'),
    ('story', 'story'),
    ('comment', 'comment'),
    ('poll', 'poll'),
    ('pollopt', 'pollopt'),
)

textWidget = forms.TextInput(attrs={
    'class': "form-control",
    'style': 'max-width: 300px;',
    'placeholder': 'Enter text to search...'
})


class StoryFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr="icontains",
                       label='Title',  widget=textWidget)
    news_type = MultipleChoiceFilter(choices=CHOICES,
                                     widget=forms.CheckboxSelectMultiple
                                     )

    class Meta:
        model = Story
        fields = ['title', 'news_type']
