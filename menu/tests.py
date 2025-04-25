from django.test import TestCase
from .models import Menu, MenuItem


class MenuTest(TestCase):
    def test_menu_creation(self):
        menu = Menu.objects.create(name="main")
        self.assertEqual(str(menu), "main")
