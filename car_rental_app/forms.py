import django.forms as forms
from car_rental_app.models import Client, STATUS, Car, CARCLASS, CHILD_SEAT, INSURENCE,ENGINE_TYPE,BODY_TYPE, STATUS, D_STATUS,D_QUANTITY,D_TYPE, Reservation, Y_N, DamagePart
from django.core.validators import EmailValidator, URLValidator, ValidationError
from .validators import validate_dlnum, validate_idnum, validate_login
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class ClientForm(forms.Form):
    name = forms.CharField(max_length=32, label="name")
    surname = forms.CharField(max_length=32, label="surname")
    strname = forms.CharField(max_length=32, label="street name")
    homenum = forms.CharField(max_length=32, label="home number")
    flatnum = forms.IntegerField(label="flat number", required=False)
    idnum = forms.CharField(max_length=9, label="ID number", validators=[validate_idnum])
    dlnum = forms.CharField(max_length=12, label="Drivin licens number", validators=[validate_dlnum])
    pesel = forms.IntegerField(label="Pesel")
    email = forms.CharField(max_length=32, label="e-mail", validators=[EmailValidator])
    phonenum = forms.IntegerField(label="phone number")

class RentOptions(forms.Form):
    reservation = forms.ModelChoiceField(queryset=Reservation.objects.all(), label="Choose reservation")
    start_date = forms.DateField(widget=forms.HiddenInput, label="Starting date:")
    end_date = forms.DateField(widget=forms.HiddenInput, label="Ending date:")
    class_car = forms.ChoiceField(widget=forms.HiddenInput, choices=CARCLASS)
    child_seat = forms.MultipleChoiceField(choices=CHILD_SEAT, label="Additional seats for child")
    add_dr = forms.BooleanField(label="Additional driver:")
    abolition = forms.BooleanField(label="Abolition from own contribution to damage")
    additional_insurence = forms.ChoiceField(choices=INSURENCE, label="Additional insurence")

class CarDamageForm(forms.Form):
    car = forms.ModelChoiceField(queryset=Car.objects.all())
    driver = forms.ModelChoiceField(queryset=Client.objects.all())
    date = forms.DateField(widget=forms.SelectDateWidget,label="Date of accident:")
    title = forms.CharField(label="Title:")
    d_note = forms.CharField(widget=forms.Textarea, label="Damages description:")
    damage_parts = forms.ModelMultipleChoiceField(DamagePart.objects.all())
    d_status = forms.ChoiceField(choices=D_STATUS, label="Damage status:")

class AddCarForm(forms.Form):
    brand = forms.CharField(max_length=16, label="Name")
    car_model = forms.CharField(max_length=16, label="Model")
    body_type = forms.ChoiceField(choices=BODY_TYPE, label="Body type")
    car_class = forms.ChoiceField(choices=CARCLASS, label="Car class")
    engine_type = forms.ChoiceField(choices=ENGINE_TYPE, label="Engine Type")
    eng_capicity = forms.DecimalField(max_digits=2, decimal_places=1, label="Engine capicity")
    hp = forms.IntegerField(label="Horse Power:")
    y_production = forms.DateField(widget=forms.SelectDateWidget, label="Date of production:")
    vin = forms.CharField(max_length=14, label="Vin")
    reg_plates = forms.CharField(max_length=8, label="Registration Plates")
    car_inspection = forms.DateField(widget=forms.SelectDateWidget,label="Car inspection valifation date")
    insurence = forms.DateField(widget=forms.SelectDateWidget ,label="Car insurence validation date")
    millage = forms.IntegerField(label="millage")
    next_service = forms.IntegerField(label="Next service at millage")
    p_capicity = forms.IntegerField(label="Number of seats")
    num_of_doors = forms.IntegerField(label="Number of doors")
    damage = forms.ChoiceField(choices=D_QUANTITY, label="Damages:")
    status = forms.ChoiceField(choices=STATUS,label="Car Status")

class AddReservation(forms.Form):
    car = forms.ModelChoiceField(queryset=Car.objects.all(), label="Car:")
    driver = forms.ModelChoiceField(queryset=Client.objects.all(), label="Driver:")
    start_date = forms.DateField(widget=forms.SelectDateWidget, label="Start date:")
    end_date = forms.DateField(widget=forms.SelectDateWidget, label="Start date:")
    start_millage = forms.IntegerField(label="Start millage:", required=False)
    end_millage = forms.IntegerField(label="End millage:", required=False)
    millage_done = forms.IntegerField(label="Millage done:", required=False)
    reservation_status = forms.ChoiceField(choices=STATUS, label="Resrvation Status")

class ReservationOptionsForm(forms.Form):
    reservation = forms.ModelChoiceField(queryset=Reservation.objects.all())
    child_seat = forms.ChoiceField(choices=CHILD_SEAT, label="Choose seats for children:", required=False)
    number_of_cs = forms.IntegerField(label="Number of child seats", required=False)
    additional_driver = forms.ChoiceField(choices=Y_N,label="Additional driver")
    abolition = forms.ChoiceField(choices=Y_N, label="Abolition of deductible in the damage")
    insurence = forms.ChoiceField(choices=INSURENCE, label="Insurence")

class UserAddForm(forms.Form):
    login = forms.CharField(label='Login', validators=[validate_login])
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat Password')
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField(label='Surname')
    email = forms.CharField(label='Email', validators=[EmailValidator()])
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise ValidationError('Hasło nie jest takie same!')
        else:
            return cleaned_data


class ClientAskForm(forms.Form):
    car_class = forms.ChoiceField(choices=CARCLASS)
    start_date = forms.DateField(widget=forms.DateField, label="Starting date:")
    end_date = forms.DateField(widget=forms.DateField, label="Ending date:")
    child_seat = forms.ChoiceField(choices=CHILD_SEAT, label="Choose seats for children:", required=False)
    number_of_cs = forms.IntegerField(label="Number of child seats", required=False)
    additional_driver = forms.ChoiceField(choices=Y_N, label="Additional driver")
    abolition = forms.ChoiceField(choices=Y_N, label="Abolition of deductible in the damage")
    insurence = forms.ChoiceField(choices=INSURENCE, label="Insurence")
    name = forms.CharField(max_length=32, label="name")
    surname = forms.CharField(max_length=32, label="surname")
    email = forms.CharField(max_length=32, label="e-mail", validators=[EmailValidator])
    phonenum = forms.IntegerField(label="phone number")


class LoginUser(forms.Form):
    login = forms.CharField(max_length=64, label="login")
    password = forms.CharField(widget=forms.PasswordInput, label="password")

class AddPartForm(forms.Form):
    part = forms.CharField(max_length=32)