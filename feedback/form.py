from django import forms

from feedback.models import OffersModel


class OfferForm(forms.ModelForm):
    class Meta:
        model = OffersModel
        fields = ('title', 'description')


class ProblemsForm(forms.Form):
    class Meta:
        model = OffersModel
        fields = ('title', 'description', 'problems')
