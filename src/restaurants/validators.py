from django.core.exceptions import ValidationError


def validate_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError("We do not accept edu emails")


CATEGORIES =['American', 'English', 'Greek', 'Asian', 'Italian']


def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f'{value} not a valid category')
