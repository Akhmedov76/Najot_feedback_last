from modeltranslation.translator import TranslationOptions, register
from .models import OffersModel, ProblemsModel


@register(OffersModel)
class OffersModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


# translator.register(OffersModel, OffersModelTranslationOptions)


@register(ProblemsModel)
class ProblemsModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
