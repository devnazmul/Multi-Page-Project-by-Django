from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exisits_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")


class AboutPageTests(SimpleTestCase):
    def test_url_exisits_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")


class PortfolioPageTests(SimpleTestCase):
    def test_url_exisits_at_correct_location(self):
        response = self.client.get("/portfolio/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("portfolio"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("portfolio"))
        self.assertTemplateUsed(response, "portfolio.html")


class ContactPageTests(SimpleTestCase):
    def test_url_exisits_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")
