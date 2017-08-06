import unittest
from django.test import TestCase
from freegeek.models import Appointment
from freegeek.models import Station
from freegeek.models import Location


class LocationTestCase(TestCase):
    def setup(self):
        Location.objects.create(location_name = 'Location B')

    def test_location_str(self):
        location_b = Location.objects.get(location_name = 'Location B')
        self.assertEqual(location_b.__str__(), 'Location B')


class StationTestCase(TestCase):
    def setup(self):
        location_a = Location.objects.create(location_name = 'Location A')
        Station.objects.create(station_name = 'data destruction', location_name = location_a)

    def test_station_str(self):
        data_destruction = Station.objects.get(station_name = 'data destruction', location_name = 'Location A')
        self.assertEqual(data_destruction.__str__(), 'data destruction')


class AppointmentTestCase(TestCase):
    def setUp(self):
        # Location.objects.create()
        location_c = Location.objects.create(location_name = 'Location C')
        recycling = Station.objects.create(station_name='recycling', location= location_c)
        Appointment.objects.create(start_time = '2017-07-31 09:15', end_time = '2017-07-31 11:15', filled = False, proficiency= 'LEVEL1', station = recycling)

    def test_appointment_str(self):
        """Testing that appointment string is returned with correct info and is grammatically correct"""
        appointment1 = Appointment.objects.get(start_time = '2017-07-31 09:15', end_time = '2017-07-31 11:15', filled = False, proficiency= 'LEVEL1',  station = 'recycling')
        self.assertEqual(appointment1.__str__(), 'Appointment: 2017-07-31 09:15 to 2017-07-31 11:15 at recycling in location C requires LEVEL1')
#






# To run tests run python manage.py test tests to run all || python manage.py test tests test_models to just run this file

