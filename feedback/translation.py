from modeltranslation.translator import TranslationOptions, register

from .models import OffersModel, ProblemsModel, AboutSiteModel, QuestionModel, TeamAboutModul, AppealsModule


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


@register(QuestionModel)
class QuestionModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(TeamAboutModul)
class TeamAboutModulTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AppealsModule)
class AppealsModuleTranslationOptions(TranslationOptions):
    fields = ('title', 'role', 'description')
