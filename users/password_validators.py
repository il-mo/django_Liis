from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class CaptialValidator:
    def __init__(
            self,
            number_of_capitals=1,

    ):
        self.number_of_capitals = number_of_capitals

    def validate(self, password, user=None):
        capitals = [char for char in password if char.isupper()]

        if len(capitals) < self.number_of_capitals:
            raise ValidationError(
                _(
                    "This password must contain at least %(min_length)d capital letters."
                ),
                code='password_too_short',
                params={'min_length': self.number_of_capitals},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(number_of_capitals)d capital letters."
            % {
                'number_of_capitals': self.number_of_capitals,
            }
        )
