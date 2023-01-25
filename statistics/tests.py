from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from statistics.models import Statistics


class ViewsTestCase(APITestCase):
    create = reverse('create')
    list = reverse('list')

    def setUp(self):
        self.statistics_1 = Statistics.objects.create(views=10, clicks=10, cost='10.10')
        self.statistics_2 = Statistics.objects.create(views=11, clicks=11, cost='11.10')
        self.statistics_3 = Statistics.objects.create(views=12, clicks=12, cost='12.10')

    def test_create(self):
        data = {'views': 12, 'clicks': 12, 'cost': '12.10'}
        response = self.client.post(self.create, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        reset = reverse('reset', args=(self.statistics_1.pk,))
        response = self.client.delete(reset)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ModelTestCase(APITestCase):
    def setUp(self):
        self.statistics_1 = Statistics.objects.create(views=10, clicks=11, cost='10.10')

    def test_creation_valid(self):
        self.assertEquals(self.statistics_1.views, 10)
        self.assertEquals(self.statistics_1.clicks, 11)
        self.assertEquals(self.statistics_1.cost, '10.10')
