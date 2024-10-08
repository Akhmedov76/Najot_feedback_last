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
    title = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
