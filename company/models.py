from django.db import models

from integra.models import BaseModel

class Company(BaseModel):    
    cnpj = models.CharField(
        max_length=18, 
        unique=True, 
        verbose_name="CNPJ"
    )
    legal_name = models.CharField(
        max_length=255, 
        verbose_name="Razão Social"
    )
    
    trade_name = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Nome Fantasia"
    )
    address = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Endereço"
    )

    def __str__(self):
        return self.trade_name or self.legal_name

    class Meta:
        verbose_name_plural = "Empresas"
        verbose_name = "Empresa"
