from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    insights = models.TextField(null=True)

    def __str__(self):
        return _(f'Feedback by -')
