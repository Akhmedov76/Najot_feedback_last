from django.db import models
from django.utils.translation import gettext_lazy as _


class OffersModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='offers_title', unique=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")


class ProblemsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='problems_title', unique=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Problem")
        verbose_name_plural = _("Problems")


class AboutSiteModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='about_site_title')
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("About Site")
        verbose_name_plural = _("About Sites")


class QuestionModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='question_title', unique=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")


class TeamAboutModul(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name', null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='team_avatars/',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Team About Module")
        verbose_name_plural = _("Team About Modules")


class AppealsModule(models.Model):
    title = models.CharField(max_length=255, verbose_name='appeals_module_title', null=True)
    role = models.CharField(max_length=255, verbose_name='role_title', null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='appeals_images/', verbose_name=_('Profile Image'), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Appeals Module")
        verbose_name_plural = _("Appeals Modules")
