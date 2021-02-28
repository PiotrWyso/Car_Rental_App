from django.db import models

# Create your models here.
CARCLASS = (
    ('premium', 'Premium'),
    ('hatchback', 'Hatchback'),
    ('city_cars', 'Small Car'),
    ('mpv', 'MPV'),
    ('van', 'Cargo Van')
)

STATUS = (
    ('free', 'Free'),
    ('service', 'In Service'),
    ('torefuel', 'To refuel'),
    ('needwash', 'Need wash'),
    ('booked', 'Booked'),
    ('blocked', 'Blocked')
)

ENGINE_TYPE = (
    ('diesel', 'Diesel'),
    ('petrol', 'Petrol'),
    ('fullhybrid', 'FullHybrid'),
    ('semihybrid', 'SemiHybrid'),
    ('electric', 'Electric')
)

BODY_TYPE = (
    ('limusine','Limusine'),
    ('combi', "Combi"),
)

INSURENCE = (
    ('standard', 'Standard'),
    ('extended', 'Extended')
)

POSITION = (
    ("fleetmanager", "Fleetmanager"),
    ('office_worker', 'Office Worker'),
)

CHILD_SEAT = (
    ("e", "-----------"),
    ("a", "0-9kg"),
    ("b", "9-18kg"),
    ("c", "18-36kg"),
    ("d", "pad"),

)

RESERVATION_STATUS = (
    ('unconfirmed', 'Unconfirmed'),
    ('confirmed', 'Confirmed'),
    ('released', 'Released'),
    ('returned', 'Returned'),
)

D_STATUS = (
    ('reapaird', "Reapaird"),
    ('unreapaird', 'Unreapaird')
)

D_TYPE = (
    ('body', 'Body'),
    ('engine', 'Engine'),
    ('electric', 'Electric'),
    ('chasis', 'Chasis')
)

D_QUANTITY = (
    ('free_of_damages', 'Free of damages'),
    ('damaged', 'Damaged')
)

Y_N = (
    ('YES', 'yes'),
    ('NO', 'no'),
)




########################################################################################################################

#                                        KLIENT


class Client(models.Model):
    name = models.CharField(max_length=32, verbose_name="name", default=None)
    surname = models.CharField(max_length=32, verbose_name="surname", default=None)
    strname = models.CharField(max_length=32, verbose_name="street name", default=None)
    homenum = models.CharField(max_length=32, verbose_name="home number", default=None)
    flatnum = models.IntegerField(verbose_name="flat number", blank=True, null=True)
    idnum = models.CharField(max_length=9, unique=True, verbose_name="ID number", default=None)
    dlnum = models.CharField(max_length=12, unique=True, verbose_name="Drivin licens number", default=None)
    pesel = models.BigIntegerField(unique=True, verbose_name="Pesel", default=None)
    email = models.CharField(max_length=32, unique=True, verbose_name="e-mail")
    phonenum = models.IntegerField(unique=True, verbose_name="phone number")

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


########################################################################################################################

#                                        SAMOCHÓD


class Car(models.Model):
    brand = models.CharField(max_length=16, verbose_name="Name")
    car_model = models.CharField(max_length=16, verbose_name="Model")
    car_class = models.CharField(max_length=32, choices=CARCLASS, verbose_name="Car class")
    body_type = models.CharField(max_length=32, choices=BODY_TYPE, verbose_name="Body type")
    engine_type = models.CharField(max_length=32, choices=ENGINE_TYPE, verbose_name="Engine Type")
    eng_capicity = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Engine capicity")
    hp = models.IntegerField(default=None, verbose_name="Horse power:")
    d_production = models.DateField(verbose_name="Date of production", default=None)
    reg_plates = models.CharField(max_length=8, unique=True, verbose_name="Registration Plates")
    vin = models.CharField(max_length=14, unique=True, verbose_name="Vin")
    millage = models.IntegerField(verbose_name="millage")
    next_service = models.IntegerField(verbose_name="Next service at millage")
    car_inspection = models.DateField(verbose_name="Car inspection valifation date")
    insurence = models.DateField(verbose_name="Car insurence validation date")
    p_capicity = models.IntegerField(verbose_name="Number of seats")
    num_of_doors = models.IntegerField(verbose_name="Number of doors")
    damage = models.CharField(max_length=32, choices=D_QUANTITY, verbose_name="Damages")
    status = models.CharField(max_length=32, choices=STATUS, verbose_name="Car Status", default="free")

    def __str__(self):
        return "{} {} {}".format(self.brand, self.car_model, self.reg_plates)


########################################################################################################################

#                                        DAMAGE TYPE

class DamagePart(models.Model):
    part = models.CharField(max_length=50)
    def __str__(self):
        return "{}".format(self.part)

########################################################################################################################

#                                       CARDAMAGE


class CarDamage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    date = models.DateField(verbose_name="Date of accident")
    d_status = models.CharField(max_length=16, choices=D_STATUS, default="repaird")
    damage_part = models.ManyToManyField(DamagePart)
    title = models.CharField(max_length=64, verbose_name="Title", default=None)
    d_note = models.TextField(default=None, verbose_name="Damages description")
    def __str__(self):
        return "{}{}".format(self.date, self.title)



########################################################################################################################

#                                        RESRVATIONS


class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    start_date = models.DateField(verbose_name="Start of rent")
    end_date = models.DateField(verbose_name="End of rent")
    start_millage = models.IntegerField(default=None, null=True)
    end_millage = models.IntegerField(default=None, null=True)
    millage_done = models.IntegerField(default=None, null=True)
    reservation_status =models.CharField(max_length=16, default="Unconfirmed")


    def __str__(self):
        return "{} {} {}".format(self.driver, self.start_date, self.car)



########################################################################################################################

#                                        RESERVATION OPTIONS


class ReservationOptions(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, primary_key=True, default=None)
    child_seat = models.CharField(max_length=32, choices=CHILD_SEAT, verbose_name="Choose child seats:", blank=True)
    number_of_cs = models.IntegerField(verbose_name="Number of child seats", blank=True)
    additional_driver = models.CharField(max_length=32, choices=Y_N, verbose_name="Additional driver")
    abolition = models.CharField(max_length=32, choices=Y_N, verbose_name="Abolition")
    insurence = models.CharField(max_length=32, choices=INSURENCE, default=None, verbose_name="Choose type of insurence", blank=True)



########################################################################################################################

#                                        CLIENT_ASK


class ClientAsk(models.Model):
    car_class = models.CharField(max_length= 32, choices= CARCLASS, default=None, verbose_name="Car class")
    start_date = models.DateField(verbose_name="Start of rent")
    end_date = models.DateField(verbose_name="End of rent")
    child_seat = models.CharField(max_length=32, choices=CHILD_SEAT, verbose_name="Choose child seats:", blank=True, default="None")
    number_of_cs = models.IntegerField(verbose_name="Number of child seats", blank=True, default=0)
    additional_driver = models.CharField(max_length=32, choices=Y_N, verbose_name="Additional driver", default="no")
    abolition = models.CharField(max_length=32, choices=Y_N, verbose_name="Abolition", default="no")
    insurence = models.CharField(max_length=32, choices=INSURENCE,
                                 verbose_name="Choose type of insurence", blank=True)
    name = models.CharField(max_length=32, verbose_name="name", blank=True)
    surname = models.CharField(max_length=32, verbose_name="surname", blank=True)
    email_q = models.CharField(max_length=32, verbose_name="e-mail", blank=True)
    phonenum_q = models.IntegerField( verbose_name="phone number", blank=True, default=0)


########################################################################################################################

