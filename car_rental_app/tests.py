from django.test import TestCase
import pytest
from car_rental_app.models import ClientAsk, Client, CarDamage, DamagePart
from django.contrib.auth.models import User, Permission
# Create your tests here.

#dodawanie zapytania
@pytest.mark.django_db
def test_client_ask(client):
    response = client.post('/res_inq_add/', {'car_class': 'mpv', 'start_date': '2021-02-28', 'end_date': '2021-03-02'})
    print(response.content)
    assert ClientAsk.objects.filter(start_date='2021-02-28')

@pytest.mark.django_db
def test_add_client(client, authorized_user):
    client.force_login(authorized_user)
    response = client.post('/client_form/', {'name': 'Andrzej', 'surname': 'Golota', 'strname' : 'Koeniga', 'homenum' : '23',
                                             'flatnum' : '23', 'idnum' : 'AWX674823', 'dlnum' : '4563/23/8947', 'pesel' : '56022407008',
                                             'email' : 'rossfriends@fox.tv', 'phonenum' : '513434434'})
    print(response.content)
    assert Client.objects.filter(flatnum='23')

@pytest.mark.django_db
def test_add_car_missing_permission(client, unauthorized_user):
    client.force_login(unauthorized_user)
    response = client.post('/Add_car', {'brand':'opel'})
    print(response.content)
    assert response.status_code == 403

@pytest.mark.django_db
def test_add_damage_part(client, authorized_user1):
    client.force_login(authorized_user1)
    response = client.post('/part_add/', {'part': 'front window'})
    print(response.content)
    assert DamagePart.objects.filter(part='front window')

@pytest.mark.django_db
def test_add_damage_car(client, authorized_user1, test_car, test_client, test_part):
    client.force_login(authorized_user1)
    response = client.post("/Add_damage", {'date': '2021-02-13', 'd_status': 'unreapaird', 'title': 'Stolen mirror', 'd_note': "Left mirror has been stolen on parking lot", 'car': [test_car.id], 'driver': [test_client.id], 'damage_parts_id': [[test_part.id]]})
    print(response.content)
    assert CarDamage.objects.filter(title="Stolen mirror")

@pytest.mark.django_db
def test_update_reservation(client, unauthorized_user, test_reservation):
    client.force_login(unauthorized_user)
    response = client.post(f'Reservation_Edit/<int:{test_reservation.id}>', {'start_date':'2021-01-12'})
    print(response.content)
    assert response.status_code == 403