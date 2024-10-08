from modeltranslation.translator import translator, TranslationOptions, register
from .models import OffersModel


@register(OffersModel)
class OffersModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

# translator.register(OffersModel, OffersModelTranslationOptions)
