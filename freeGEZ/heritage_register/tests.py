# from django.test import TestCase
#
# from django.urls import reverse
# from .models import Relic
#
#
# class TempleTest(TestCase):
#
#     def test_reverse_home(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'heritage_register/home.html')
#
#     def test_create_card(self):
#         data = {
#             'name': 'Pałac',
#             'time_of_creation': 'epoka żelaza',
#             'place': 'Pcim',
#             'address': 'ul. śmaka',
#             'municipality': 'zzz',
#             'forms_of_protection': 'to to i to',
#             'description': 'widok',
#         }
#         response = self.client.post('/relic/', data)
#         #self.assertEqual(response.status_code, 201)
#         print(response.content)
#         self.assertEqual(response, data['name'])
