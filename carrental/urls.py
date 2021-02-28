"""carrental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from car_rental_app.views import ClientFormView, AddCarView, CarView, AddDamgeView, ClientView, CarsView,\
                               CarUpdateViewByAutoView, ClientUpdateViewByAutoView, ClientsView, CarDeleteViewByAutoView,\
                                ClientDeleteViewByAutoView, AddReservationView, ReservationDeleteViewByAutoView,\
                                ResrvationsView, ReservationView, ResrvationUpdateViewByAutoView, DamagesUpdateViewByAutoView,\
                                DamagesView, DamageView, OptionsAddFormView, OptionView, OptionDeleteViewByAutoView,\
                                OptionUpdateViewByAutoView, ResInqCreateViewByAutoView, ResInqUpdateViewByAutoView,\
                                ResInq1UpdateViewByAutoView, ResInqView, ResInqAllView, ResInqDeleteViewByAutoView, AddUserView,\
                                LogOut, LoginUserView, AboutUsView, FleetView, AddPartView, AddPartsDamageView

urlpatterns = [
    path('admin/', admin.site.urls),


    #####CAR#####
    path('car_confirm_delete/<int:pk>', CarDeleteViewByAutoView.as_view()),
    path('Add_car', AddCarView.as_view()),
    path('Car_view/<int:car_id>/', CarView.as_view()),
    path('cars_view/', CarsView.as_view()),
    path('edit_car/<int:pk>/', CarUpdateViewByAutoView.as_view()),

    #####DAMAGE#####
    path('Add_damage', AddDamgeView.as_view()),
    path('edit_car_damage/<int:pk>', DamagesUpdateViewByAutoView.as_view()),
    path('Damages/', DamagesView.as_view()),
    path('damage/<int:damage_id>', DamageView.as_view()),

    #####CLIENT#####
    path('Client/<int:client_id>/', ClientView.as_view()),
    path('edit_client/<int:pk>/', ClientUpdateViewByAutoView.as_view()),
    path('clients/', ClientsView.as_view()),
    path('client_confirm_delete/<int:pk>', ClientDeleteViewByAutoView.as_view()),
    path('client_form/', ClientFormView.as_view()),

    #####RESERVATION#####
    path('Add_Reservation/', AddReservationView.as_view()),
    path('Reservation_Edit/<int:pk>', ResrvationUpdateViewByAutoView.as_view()),
    path('reservation_confirm_delete/<int:pk>', ReservationDeleteViewByAutoView.as_view()),
    path('Reservations/', ResrvationsView.as_view()),
    path('reservation_view/<int:reservation_id>', ReservationView.as_view()),

    #####RES OPTIONS#####
    path('add_option/', OptionsAddFormView.as_view()),
    path('option_view',OptionView.as_view()),
    path('option_confirm_delete/<int:pk>', OptionDeleteViewByAutoView.as_view()),
    path('option_edit/<int:pk>', OptionUpdateViewByAutoView.as_view()),

    #####USER#####
    path('add_user/', AddUserView.as_view()),
    path('login/', LoginUserView.as_view()),
    path('logout/', LogOut.as_view()),

    #####CLIENT INQ######
    path('res_inq_add/', ResInqCreateViewByAutoView.as_view()),
    path('edit_res_inq/<int:pk>', ResInqUpdateViewByAutoView.as_view(), name='up_res_inq'),
    path('edit_res_inq1/<int:pk>', ResInq1UpdateViewByAutoView.as_view(), name='up_res_inq1'),
    path('res_inq_confirm_delete/<int:pk>', ResInqDeleteViewByAutoView.as_view()),
    path('res_inq_all/', ResInqAllView.as_view()),
    path('res_inq/<int:resinq_id>', ResInqView.as_view()),
    # path('res_inq_added/', view)

    ##### MAIN #####
    path('about_us/', AboutUsView.as_view()),
    path('fleet_view/', FleetView.as_view()),

    ##### PARTS #####
    path('part_add/', AddPartView.as_view()),
    path('damage_part/', AddPartsDamageView.as_view())
]
