from modeltranslation.translator import TranslationOptions, register

from .models import OffersModel, ProblemsModel, AboutSiteModel


@register(OffersModel)
class OffersModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


# translator.register(OffersModel, OffersModelTranslationOptions)


@register(ProblemsModel)
class ProblemsModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutSiteModel)
class AboutSiteModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
