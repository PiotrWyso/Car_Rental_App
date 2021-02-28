import pytest
from django.contrib.auth.models import User, Permission
from car_rental_app.models import Client, Car, Reservation, CarDamage, DamagePart


@pytest.fixture
def authorized_user():
    authorized_user = User.objects.create_user("Wilk")
    perm = Permission.objects.get(codename="add_client")
    authorized_user.user_permissions.add(perm)
    return authorized_user

@pytest.fixture
def authorized_user1():
    authorized_user1 = User.objects.create_user("Wilku")
    perm = Permission.objects.get(codename="add_cardamage")
    perm1 = Permission.objects.get(codename="add_reservationoptions")
    authorized_user1.user_permissions.add(perm)
    authorized_user1.user_permissions.add(perm1)
    return authorized_user1

@pytest.fixture
def unauthorized_user():
    unauthorized_user = User.objects.create_user("Wilk")
    return unauthorized_user

@pytest.fixture
def test_car():
    car = Car.objects.create(brand="Mitsubishi", car_model="Colt", car_class="hatchback", body_type="combi", engine_type="petrol",eng_capicity="1.4", hp="90", d_production="2009-04-12",
                             reg_plates="ETM75406", vin="12345678901234", millage="20323",next_service="30000",car_inspection="2021-04-05",insurence="2021-03-27",
                             p_capicity="4", num_of_doors="5", damage="free_of_damages", status="free")
    return car

@pytest.fixture
def test_reservation():
    car = Car.objects.create(brand="Mitsubishi", car_model="Colt", car_class="hatchback", body_type="combi",
                             engine_type="petrol", eng_capicity="1.4", hp="90", d_production="2009-04-12",
                             reg_plates="ETM75406", vin="12345678901234", millage="20323", next_service="30000",
                             car_inspection="2021-04-05", insurence="2021-03-27",
                             p_capicity="4", num_of_doors="5", damage="free_of_damages", status="free")

    client = Client.objects.create(name="Aleks", surname="Nowak", strname="Bobra", homenum="89", flatnum="33",
                                   idnum="TRE435265", dlnum="7465/76/5364", pesel="56021276358", email="nie@dobrze.pl",
                                   phonenum="576893021")

    reservation = Reservation.objects.create(start_date="2021-02-13", end_date="2021-02-16",reservation_status="booked", driver_id=f"{car.id}", car_id=f'{client.id}')
    return reservation

@pytest.fixture
def test_damage():
    car = Car.objects.create(brand="Mitsubishi", car_model="Colt", car_class="hatchback", body_type="combi",
                             engine_type="petrol", eng_capicity="1.4", hp="90", d_production="2009-04-12",
                             reg_plates="ETM75406", vin="12345678901234", millage="20323", next_service="30000",
                             car_inspection="2021-04-05", insurence="2021-03-27",
                             p_capicity="4", num_of_doors="5", damage="free_of_damages", status="free")

    client = Client.objects.create(name="Aleks", surname="Nowak", strname="Bobra", homenum="89", flatnum="33",
                                   idnum="TRE435265", dlnum="7465/76/5364", pesel="56021276358", email="nie@dobrze.pl",
                                   phonenum="576893021")

    damage = CarDamage.objects.create(date="2021-02-15", d_status="reapaird", title="Parking Accident", d_note="Small scratch on rear bumper", car=f'{car.id}', driver=f'{client.id}')
    return damage

@pytest.fixture
def test_part():
    damage_part = DamagePart.objects.create(part='left mirror')
    return damage_part

@pytest.fixture
def test_client():
    client = Client.objects.create(name="Aleks", surname="Nowak",strname="Bobra", homenum="89", flatnum="33", idnum="TRE435265", dlnum="7465/76/5364",pesel="56021276358", email="nie@dobrze.pl", phonenum="576893021")
    return client