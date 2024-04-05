from django.test import TestCase
from django.urls import reverse
from Restaurant.models import Menu
import json


class MenuViewTest(TestCase):
    
    def setUp(self):
        Menu.objects.create(title="IceCream", price=4.50, inventory=20)
        Menu.objects.create(title="Cake", price=3.75, inventory=15)
        
    def test_getall(self):
        response = self.client.get(reverse('menu_list'))
        self.assertEqual(response.status_code, 200)
        
        actual_data = response.json()
        # Remove the 'id' field from each dictionary in the response data
        for item in actual_data:
            item.pop('id', None)
        
        expected_data = [
            {"title": "IceCream", "price": "4.50", "inventory": 20},
            {"title": "Cake", "price": "3.75", "inventory": 15}
        ]
        
        self.assertJSONEqual(json.dumps(sorted(response.json(), key=lambda x: x['title'])),
                             json.dumps(sorted(expected_data, key=lambda x: x['title'])))

