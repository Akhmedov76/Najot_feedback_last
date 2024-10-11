from django import forms

from feedback.models import OffersModel, ProblemsModel, AboutSiteModel, TeamAboutModul, QuestionModel, AppealsModule


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


class TeamAboutForm(forms.ModelForm):
    class Meta:
        model = TeamAboutModul
        fields = ('title', 'description')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = ('title', 'description')


class AppealsForm(forms.ModelForm):
    class Meta:
        model = AppealsModule
        fields = ('title', 'role', 'description', 'image',)
