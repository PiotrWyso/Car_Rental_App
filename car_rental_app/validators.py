from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy
import re

# def validate_pesel(pesel):
#         weights = [1, 3, 7, 9,
#                    1, 3, 7, 9, 1, 3]
#         weight_index = 0
#         digits_sum = 0
#         for digit in pesel[: -1]:
#             digits_sum += int(digit) * weights[weight_index]
#             weight_index += 1
#         pesel_modulo = digits_sum % 10
#         validate = 10 - pesel_modulo
#         if validate != 10:
#             raise ValidationError(
#                 'You have wrote wrong PESEL number'
#             )

def validate_idnum(idnum):
    resAZ = re.match('[A-Za-z]{3}[0-9]{6}', idnum)

    if len(idnum) > 9:
        raise ValidationError(
            'Yours id number is to long!'
        )
    elif resAZ == None:
        raise ValidationError(
            'Check Your ID number!'
        )


def validate_dlnum(dlnum):
    check_dl = re.match('[0-9]{4}([0-9]{2})?\/[0-9]{2}([0-9]{2})?\/[0-9]{4}([0-9]{2})?', dlnum)
    if check_dl == None:
        raise ValidationError(
            'Check Your driving licens number!'
        )

def vin_validator(vin):
    if len(vin)!=15:
        raise ValidationError(
            'Check car VIN number!'
        )

def validate_login(login):
    if User.objects.filter(username=login):
        raise ValidationError('Podany użytkownik już istnieje!')