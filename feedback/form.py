from django import forms

from feedback.models import OffersModel, ProblemsModel,AboutSiteModel


class OfferForm(forms.ModelForm):
    class Meta:
        model = OffersModel
        fields = ('title', 'description')


class ProblemsForm(forms.ModelForm):
    class Meta:
        model = ProblemsModel
        fields = ('title', 'description')


class AboutSiteForm(forms.ModelForm):
    class Meta:
        model = AboutSiteModel
        fields = ('title', 'description')