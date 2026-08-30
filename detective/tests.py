from django.test import TestCase
from django.urls import reverse
from .models import Case


class CaseViewTest(TestCase):

    def setUp(self):
        self.case = Case.objects.create(
            title="The Missing Laptop",
            description="A laptop disappeared from the library.",
            location="College Library",
            difficulty="Medium"
        )

    def test_case_list(self):
        response = self.client.get(reverse('case_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Missing Laptop")

    def test_case_detail(self):
        response = self.client.get(
            reverse('case_detail', args=[self.case.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Missing Laptop")

    def test_case_not_found(self):
        response = self.client.get(
            reverse('case_detail', args=[999])
        )

        self.assertEqual(response.status_code, 404)