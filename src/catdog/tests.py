from django.test import TestCase
from django.urls import reverse


class TestCatDogView(TestCase):
    def test_get(self):
        result = self.client.get(reverse('catdog'))
        self.assertEqual(result.status_code, 200)
        self.assertTemplateUsed(result, template_name='catdog.html')

    def test_post_cat(self):
        result = self.client.post(reverse('catdog'), {'cat': 'true'})
        self.assertEqual(result.status_code, 200)
        self.assertTemplateUsed(result, template_name='pet.html')