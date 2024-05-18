from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name=_('ID')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Data de criação')
    )
    class Meta:
        abstract = True
