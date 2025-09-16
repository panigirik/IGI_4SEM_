from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Destination, Hotel, Client, Tour
from datetime import date

class BookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client_profile = Client.objects.create(
            user=self.user,
            patronymic='Ivanovich',
            address='123 Main St',
            phone='1234567890'
        )
        self.destination = Destination.objects.create(
            name='Tokyo',
            img='pics/tokyo.jpg',
            desc='Modern city',
            price=1000,
            offer=True
        )
        self.hotel = Hotel.objects.create(
            name='Tokyo Grand',
            destination=self.destination,
            stars=5
        )

    def test_destination_str(self):
        self.assertEqual(str(self.destination), 'Tokyo')

    def test_hotel_str(self):
        self.assertEqual(str(self.hotel), 'Tokyo Grand (Tokyo)')

    def test_client_str(self):
        self.assertEqual(str(self.client_profile), 'testuser')

    def test_tour_creation_and_price(self):
        tour = Tour.objects.create(
            client=self.client_profile,
            destination=self.destination,
            hotel=self.hotel,
            start_date=date.today(),
            duration_weeks=2,
            total_price=0  # will be calculated
        )
        self.assertEqual(tour.total_price, 2000)
        self.assertEqual(str(tour), f"Tour for {self.client_profile} to Tokyo on {tour.start_date}")
