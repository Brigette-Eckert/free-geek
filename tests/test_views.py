import unittest
from django.test import TestCase
from django.test import RequestFactory
from freegeek.views import home
from freegeek.views import diary


class HomeViewTest(TestCase):
    '''
    Test Home View
    '''
    def setup(self):
        self.user = UserFactory()
        self.factory = RequestFactory()

    def test_get_home(self):
        '''Test GET request for home view'''
        request = self.factory.get(reverse('home'))
        request.user = self.user
        self.assertEqual(response.context_data['user'], self.user)
        self.assertEqual(response.context_data['request'], request)

class DiaryViewTest(TestCase):
    '''
    Test Diary View
    '''
    def setup(self):
        self.user = UserFactory()
        self.factory = RequestFactory()

    def test_get_diary(self):
        '''Test GET request for diary view'''
        request = self.factory.get(reverse('diary'))
        request.user = self.user
        self.assertEqual(response.context_data['user'], self.user)
        self.assertEqual(response.context_data['request'], request)
        self.assertEqual(response.context_data['request'], request)