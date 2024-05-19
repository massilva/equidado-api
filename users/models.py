from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
    COMPANY_ADMIN = 'CompanyAdmin', _('Administrador da Empresa')
    EMPLOYEE = 'Employee', _('Funcionário')


class UserModel(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    user_role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.EMPLOYEE,
    )
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='users',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'


class UserCharacteristics(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

UserModel.add_to_class('characteristics', models.ManyToManyField(UserCharacteristics, related_name='users'))
