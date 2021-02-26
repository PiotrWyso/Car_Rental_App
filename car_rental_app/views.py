from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import ClientForm, AddCarForm, CarDamageForm, AddReservation, ReservationOptionsForm, UserAddForm, LoginUser, AddPartForm
from .models import Car, CarDamage, Reservation, Client, ReservationOptions, ClientAsk, DamagePart
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.



########################################################################################################################

#                                        DODAWANIE SAMOCHODU


class AddCarView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.add_car'
    def get(self, request):
        form = AddCarForm
        return render(request, "Add_car.html", {"form": form})
    """get - views add car form"""

    def post(self, request):
        form = AddCarForm(request.POST)
        if form.is_valid():
            added_car = Car.objects.create(brand=form.cleaned_data['brand'],
                                           car_model=form.cleaned_data['car_model'],
                                           vin=form.cleaned_data['vin'],
                                           reg_plates=form.cleaned_data['reg_plates'],
                                           car_inspection=form.cleaned_data['car_inspection'],\
                                           insurence=form.cleaned_data['insurence'],
                                           millage=form.cleaned_data['millage'],
                                           next_service=form.cleaned_data['next_service'],\
                                           p_capicity=form.cleaned_data['p_capicity'],
                                           body_type=form.cleaned_data['body_type'],
                                           car_class=form.cleaned_data['car_class'],\
                                           num_of_doors=form.cleaned_data['num_of_doors'],
                                           eng_capicity=form.cleaned_data['eng_capicity'],\
                                           damage=form.cleaned_data['damage'],
                                           status=form.cleaned_data['status'],
                                           hp=form.cleaned_data['hp'],\
                                           d_production=form.cleaned_data['y_production'])

            return redirect(f'Car_view/{added_car.id}')
        else:
            return render(request, "Add_car.html", {"form": form})

    """if form is valid post is adding car to base and shows card of card, if not returns to add form"""

########################################################################################################################

#                                        WIDOK SAMOCHODU


class CarView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_car'
    def get(self, request, car_id):
        car = Car.objects.get(id=car_id)
        reservations = Reservation.objects.filter(car=car_id)
        damages = CarDamage.objects.filter(car=car_id)
        return render(request, "Car_view.html", {"car":car, "damages":damages, "reservations":reservations})

    """get - car info"""


########################################################################################################################

#                                        DODAWANIE SZKODY

class AddDamgeView(PermissionRequiredMixin, View):
        permission_required = 'car_rental_app.add_cardamage'
        def get(self, request):
            form = CarDamageForm
            return render(request, "Add_damage.html", {"form": form})

        """get - views add damage form"""

        def post(self, request):
            form = CarDamageForm(request.POST)
            if form.is_valid():
                added_damage = CarDamage.objects.create(car=form.cleaned_data["car"],
                                               driver=form.cleaned_data["driver"],
                                               date=form.cleaned_data['date'],
                                               d_status=form.cleaned_data['d_status'],
                                               title=form.cleaned_data['title'],
                                                damage_parts=form.cleaned_data['damage_parts'],
                                               d_note=form.cleaned_data['d_note']
                                               )
                return redirect(f'damage/{added_damage.id}')
            else:
                return render(request, "Add_damage.html", {"form": form})

        """if form is valid post is adding damage to base and shows card of damage, if not returns to add form"""


########################################################################################################################

#                                        DODAWANIE REZERWACJI


class AddReservationView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.add_reservation'
    def get(self, request):
        form = AddReservation
        return render(request, "Add_Reservation.html",{"form": form})
    """get - views add reservation form"""

    def post(self, request):
        form = AddReservation(request.POST)
        if form.is_valid():
            added_reservation = Reservation.objects.create(car=form.cleaned_data["car"],
                                                           driver=form.cleaned_data["driver"],
                                                           start_date=form.cleaned_data["start_date"],
                                                           end_date=form.cleaned_data["end_date"],
                                                           start_millage=form.cleaned_data['start_millage'],
                                                           end_millage=form.cleaned_data['end_millage'],
                                                           millage_done=form.cleaned_data['millage_done'],
                                                           reservation_status=form.cleaned_data['reservation_status'])
            return redirect(f'/reservation_view/{added_reservation.id}')
        else:
            return render(request, "Add_Reservation.html", {"form": form})
    """if form is valid post is adding Reservation to base and shows card of Reservation, if not returns to add form"""

########################################################################################################################

#                                        DODAWANIE KLIENTA


class ClientFormView(PermissionRequiredMixin, FormView):
    permission_required = 'car_rental_app.add_client'
    def get(self, request):
        form = ClientForm
        return render(request, "client_form.html", {"form":form})
    """get - views add Client form"""

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            added_client = Client.objects.create(
                name=form.cleaned_data["name"],
                surname=form.cleaned_data["surname"],
                strname=form.cleaned_data["strname"],
                homenum=form.cleaned_data["homenum"],
                flatnum=form.cleaned_data["flatnum"],
                idnum=form.cleaned_data["idnum"],
                dlnum=form.cleaned_data["dlnum"],
                pesel=form.cleaned_data["pesel"],
                email=form.cleaned_data["email"],
                phonenum=form.cleaned_data["phonenum"],
            )
            return redirect(f'/Client/{added_client.id}')
        else:
            return render(request, "client_form.html", {"form": form})
    """if form is valid post is adding client to base and shows card of client, if not returns to add form"""


########################################################################################################################

#                                        KLIENTVIEW

class ClientView(PermissionRequiredMixin,View):
    permission_required = 'car_rental_app.view_client'
    def get(self, request, client_id):
        client = Client.objects.get(id=client_id)
        reservations = Reservation.objects.filter(driver=client_id)
        # damages = CarDamage.objects.get(client=client_id)
        return render(request, "Client.html", {"client":client, "reservations":reservations})
    """get - views add Client info"""

########################################################################################################################

#                                        CARSVIEW

class CarsView(PermissionRequiredMixin,View):
    permission_required = 'car_rental_app.view_car'
    def get(self, request):
        cars = Car.objects.all()
        return render(request, "cars_view.html", {"cars":cars})
    """get - view list of cars"""

########################################################################################################################

#                                        CARUPDATE

class CarUpdateViewByAutoView(PermissionRequiredMixin, UpdateView):
    permission_required = 'car_rental_app.change_car'
    model = Car
    template_name = 'edit_car.html'
    fields = ['brand', 'car_model', 'car_class', 'body_type', 'eng_capicity', 'hp', 'd_production', 'reg_plates', 'vin', 'millage',
              'next_service', 'car_inspection', 'insurence', 'p_capicity', 'num_of_doors', 'damage', 'status']
    success_url = '/cars_view/'
    """UPADATE form of car, after submit it returns to car list"""

########################################################################################################################

#                                        CLIENTEDIT

class ClientUpdateViewByAutoView(PermissionRequiredMixin, UpdateView):
    permission_required = 'car_rental_app.change_client'
    model = Client
    template_name = 'edit_client.html'
    fields = ['name', 'surname', 'strname', 'homenum', 'flatnum', 'idnum', 'dlnum', 'pesel', 'email', 'phonenum']
    success_url = '/clients_view/'
    """UPADATE form of client, after submit it returns to client list"""

########################################################################################################################

#                                        CLIENTSVIEW

class ClientsView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_client'
    def get(self, request):
        clients = Client.objects.all()
        return render(request, "clients.html", {"clients":clients})

    """get - views clients list"""

########################################################################################################################

#                                        CARDELETE

class CarDeleteViewByAutoView(PermissionRequiredMixin, DeleteView):
    permission_required = 'car_rental_app.delete_car'
    model = Car
    template_name = "car_confirm_delete.html"
    success_url = '/cars_view/'
    """Delete view of car"""

########################################################################################################################

#                                        CLIENTDELETE

class ClientDeleteViewByAutoView(PermissionRequiredMixin, DeleteView):
    permission_required = 'car_rental_app.delete_client'
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = '/clients/'
    """Delete view of clients and redirects to client list"""
########################################################################################################################

#                                        RESERVATIONEDIT

class ResrvationUpdateViewByAutoView(PermissionRequiredMixin, UpdateView):
    permission_required = 'car_rental_app.change_reservation'
    model = Reservation
    template_name = 'Reservation_Edit.html'
    fields = ['car', 'driver', 'start_date', 'end_date', 'start_millage', 'end_millage', 'reservation_status']
    success_url = '/Reservations/'
    """Resrervation Update view, after update redirects us to Reservation list"""

########################################################################################################################

#                                        RESERVATIONDELETE

class ReservationDeleteViewByAutoView(PermissionRequiredMixin, DeleteView):
    permission_required = 'car_rental_app.delete_reservation'
    model = Reservation
    template_name = "reservation_confirm_delete.html"
    success_url = '/reservations_view/'
    """Resrvation delete view, redirect us to reservations view"""

########################################################################################################################

#                                        RESERVATIONSVIEW

class ResrvationsView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_reservation'
    def get(self, request):
        reservations = Reservation.objects.all()
        return render(request, "Reservations.html", {"reservations":reservations })

    """get - views reservation list"""

########################################################################################################################

#                                        RESERVATION VIEW

class ReservationView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_reservation'
    def get(self, request, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        resop = ReservationOptions.objects.filter(reservation=reservation_id)
        return render(request, "reservation_view.html", {"reservation":reservation, "resop":resop})

    """get - views reservation"""


########################################################################################################################

#                                        DAMAGES EDIT

class DamagesUpdateViewByAutoView(PermissionRequiredMixin, UpdateView):
    permission_required = 'car_rental_app.change_cardamage'
    model = CarDamage
    template_name = 'edit_car_damage.html'
    fields = ['car', 'driver', 'date', 'title', 'd_note','damage_part', 'd_status']
    success_url = '/Damages/'
    """UPADATE form of damage, after submit it returns to damage list"""

########################################################################################################################

#                                       DAMAGES VIEW

class DamagesView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_cardamage'
    def get(self, request):
        damages = CarDamage.objects.all()
        return render(request, "Damages.html", {"damages":damages})

    """get - views damages list"""


########################################################################################################################

#                                        DAMAGE VIEW

class DamageView(View):
    def get(self, request, damage_id):
        damage = CarDamage.objects.get(id=damage_id)
        return render(request, "damage.html", {"damage":damage })

    """get - views damage"""


########################################################################################################################
########################################################################################################################

#                                               RESERVATION OPTIONS

########################################################################################################################
########################################################################################################################

#                                               RESERVATION OPTIONS FORM

class OptionsAddFormView(PermissionRequiredMixin, FormView):
    permission_required = 'car_rental_app.add_reservationoptions'
    def get(self, request):
        form = ReservationOptionsForm()
        return render(request, "add_option.html", {'form': form})

    """get - views add user form"""

    def post(self, request):
        form = ReservationOptionsForm(request.POST)
        if form.is_valid():
            ReservationOptions.objects.create(reservation=form.cleaned_data['reservation'],
                                    child_seat=form.cleaned_data['child_seat'],
                                    number_of_cs=form.cleaned_data['number_of_cs'],
                                    additional_driver=form.cleaned_data['additional_driver'],
                                    abolition=form.cleaned_data['abolition'],
                                    insurence=form.cleaned_data['insurence'])
            return redirect('Reservations.html')
        else:
            return render(request, "add_option.html", {'form': form})
    """Resrvations options form, after submit redirect to Reservations list"""

########################################################################################################################

#                                               RESERVATION OPTION VIEW

class OptionView(PermissionRequiredMixin,View):
    permission_required = 'car_rental_app.view_reservationoptions'
    def get(self, request, option_id):
        option = ReservationOptions.objects.get(id=option_id)
        return render(request, "option.html", {"option":option})
    """get - shows option of reservation"""


########################################################################################################################

#                                            OPTION DELETE

class OptionDeleteViewByAutoView(PermissionRequiredMixin, DeleteView):
    permission_required = 'car_rental_app.delete_reservationoptions'
    model = ReservationOptions
    template_name = "option_confirm_delete.html"
    success_url = '/reservations_view/'
    """Delete view of option and redirects to reservation list"""



########################################################################################################################

#                                            OPTION EDIT

class OptionUpdateViewByAutoView(PermissionRequiredMixin, UpdateView):
    permission_required = 'car_rental_app.change_reservationoptions'
    model = ReservationOptions
    template_name = 'Reservation_Edit.html'
    fields = ['reservation', 'child_seat', 'number_of_cs', 'additional_driver', 'abolition', 'insurence']
    success_url = '/Reservations/'
    """option update, after submit redirect to reservation list"""




########################################################################################################################
########################################################################################################################

#                                            RESRVATION INQUIRY

class ResInqCreateViewByAutoView(CreateView):
    form = ClientAsk
    model = ClientAsk
    template_name = "res_inq_add.html"
    fields = ['car_class', 'start_date', 'end_date']
    def get_success_url(self):
        return reverse('up_res_inq', args=(self.object.id,))
    """Reservation inquiry form view which redirects to next step"""


class ResInqUpdateViewByAutoView(UpdateView):
    form = ClientAsk
    model = ClientAsk
    template_name = "edit_res_inq.html"
    fields = ['child_seat','number_of_cs', 'additional_driver', 'abolition', 'insurence']
    def get_success_url(self):
        return reverse('up_res_inq1', args=(self.object.id,))

    """Reservation inquiry form view which redirects to next step"""


class ResInq1UpdateViewByAutoView(UpdateView):
    form = ClientAsk
    model = ClientAsk
    template_name = "edit_res_inq1.html"
    fields = ['name','surname', 'email_q', 'phonenum_q']
    success_url = "/about_us"
    """Reservation inquiry form view which redirects to next step"""

class ResInqDeleteViewByAutoView(DeleteView):
    model = ClientAsk
    template_name = "res_inq_confirm_delete.html"
    success_url = '/res_inq_view/'
    """final step of adding inquiry redirect to about us"""

class ResInqAllView(View):
    def get(self, request):
        res_inq_all = ClientAsk.objects.all()
        return render(request, "res_inq_all.html", {"res_inq_all":res_inq_all})
    """get show list of inquires"""

class ResInqView(View):
    def get(self, request, resinq_id):
        resinq = ClientAsk.objects.get(id=resinq_id)
        return render(request, "res_inq.html", {"resinq":resinq})
    """get shows inquiry"""
########################################################################################################################

#                                            ADD USER


class AddUserView(View):
    def get(self, request):
        form = UserAddForm()
        return render(request, "add_user.html", {'form': form})
    """get - views add user form"""

    def post(self, request):
        form = UserAddForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['login'],
                                     password=form.cleaned_data['password'],
                                     email=form.cleaned_data['email'],
                                     first_name=form.cleaned_data['first_name'],
                                     last_name=form.cleaned_data['last_name'])
            return redirect('/login/')
        else:
            return render(request, "add_user.html", {'form': form})
    """post if form is valid redirect us to login if not to add user form"""

########################################################################################################################

#                                            USER LOG OUT

class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/about_us')
    """ logut view redirect to about us"""

########################################################################################################################

#                                            USER LOGIN

class LoginUserView(View):
    def get(self, request):
        form = LoginUser()
        return render(request, "login.html", {"form": form})
    """get - views login form"""
    def post(self, request):
        rec_form = LoginUser(request.POST)
        if rec_form.is_valid():
            user = authenticate(username = rec_form.cleaned_data["login"], password = rec_form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect('/about_us')
            else:
                return render(request, "login.html", {'form':rec_form})
        else:
            return render(request, "login.html", {'form': rec_form})
    """post - if form is valid redirect to about us if not, than to login form"""


########################################################################################################################

#                                           STATIC VIEWS

class AboutUsView(View):
    def get(self, request):
        return render(request, "about_us.html")

class FleetView(View):
    def get(self, request):
        return render(request, "fleet_view.html")


########################################################################################################################

#                                           PARTS


class AddPartView(PermissionRequiredMixin, FormView):
    permission_required = 'car_rental_app.add_cardamage'
    def get(self, request):
        form = AddPartForm()
        return render(request, "part_add.html", {'form': form})

    """get - views add user form"""

    def post(self, request):
        form = AddPartForm(request.POST)
        if form.is_valid():
            DamagePart.objects.create(part=form.cleaned_data['part'])
            return redirect('/Damages/')
        else:
            return render(request, "part_add.html.html", {'form': form})
    """Resrvations options form, after submit redirect to Reservations list"""