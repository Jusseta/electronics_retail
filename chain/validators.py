from rest_framework.serializers import ValidationError


class FactoryValidator:
    """If the factory has a provider"""
    def __init__(self, type, provider):
        self.type = type
        self.provider = provider

    def __call__(self, value):
        type = dict(value).get(self.type)
        provider = dict(value).get(self.provider)
        if type == 'FACTORY':
            if provider:
                raise ValidationError("Factory doesn't have a provider")
