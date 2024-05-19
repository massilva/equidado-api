from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password,
            )

            if not user:
                msg = _('Não foi possível fazer login com as credenciais fornecidas.')
                raise serializers.ValidationError(msg, code='authorization')

            if user.is_superuser:
                msg = _('Impossível fazer login com as credenciais fornecidas.')
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = _('Email e senha são necessários para fazer login.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
