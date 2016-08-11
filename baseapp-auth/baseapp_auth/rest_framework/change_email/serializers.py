from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from apps.users.models import User
from apps.users.tokens import ChangeEmailConfirmTokenGenerator, ChangeEmailVerifyTokenGenerator


class ChangeEmailRequestSerializer(serializers.Serializer):
    new_email = serializers.EmailField()

    def validate_new_email(self, new_email):
        if User.objects.filter(email=new_email).exists():
            raise serializers.ValidationError(_('That email is already in use.'))
        return new_email

    def create(self, validated_data):
        user = self.context['request'].user
        user.new_email = validated_data['new_email']
        user.save()
        return user


class ChangeEmailConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, token):
        if not ChangeEmailConfirmTokenGenerator().check_token(self.instance, token):
            raise serializers.ValidationError(_('Invalid token.'))
        return token

    def update(self, instance, validated_data):
        instance.is_new_email_confirmed = True
        instance.save()
        return instance


class ChangeEmailVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, token):
        if not ChangeEmailVerifyTokenGenerator().check_token(self.instance, token):
            raise serializers.ValidationError(_('Invalid token.'))
        return token

    def update(self, instance, validated_data):
        instance.email = instance.new_email
        instance.new_email = ''
        instance.is_new_email_confirmed = False
        instance.save()
        return instance