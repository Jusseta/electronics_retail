import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from chain.models import Contacts, Product, RetailChain
from users.models import User


class RetailChainTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.ru',
            password='12qw34er',
            is_active=True,
            first_name='test',
            last_name='test',
        )
        self.client.force_authenticate(user=self.user)

        self.contacts = Contacts.objects.create(
            email='testcontacts@test.ru',
            country='testcountry',
            city='testcity',
            street='teststreet',
            building='testbuilding',
        )

        self.retailchain = RetailChain.objects.create(
            name='testname1',
            type='RETAIL_NET',
            contacts=self.contacts,
            debt=100.20,
            created_at='2020-10-10'
        )

    def test_product_create(self):
        """Create test case"""
        data = {
            'name': 'testname',
            'model': 'testmodel',
            'release_date': '2020-10-20'
        }

        response = self.client.post(
            '/product/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_retailchain_create(self):
        """Create test case"""
        data = {
            'name': 'testname',
            'type': 'IND_ENTREPRENEUR',
            'contacts': self.contacts.id,
            'debt': 2.03
        }

        response = self.client.post(
            '/chain/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_contacts_list(self):
        """List test case"""
        response = self.client.get('/contacts/')

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.contacts.id,
                        "email": self.contacts.email,
                        "country": self.contacts.country,
                        "city": self.contacts.city,
                        "street": self.contacts.street,
                        "building": self.contacts.building
                    }
                ]
            }
        )

    def test_retailchain_update(self):
        """Update test case"""
        data = {
            'name': 'testnametest',
        }

        response = self.client.patch(
            f'/chain/{self.retailchain.id}/',
            data=data
        )
        print(response.json())
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retailchain_delete(self):
        """Delete test case"""
        response = self.client.delete(
            f'/chain/{self.retailchain.id}/'
        )

        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT)

    def test_factory_create(self):
        data = {
            'name': 'testname',
            'type': 'FACTORY',
            'contacts': self.contacts.id,
            'provider': 2,
            'debt': 2.03
        }

        response = self.client.post(
            '/chain/',
            data=data
        )
        print(response.json())
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
