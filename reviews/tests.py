from django.test import TestCase
from .models import Review
from django.urls import reverse


class ReviewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.review = Review.objects.create(
            title="Citizen Kane",
            director="Orson Welles",
            actors="Orson Welles and Joseph Cotten",
            review="One of the greatest films of all time, a must see. A true, timeless masterpiece.",
            year=1941,
            stars="ssss",
        )

    def test_example_title(self):
        self.assertEqual(self.review.title, "Citizen Kane")

    def test_review_director(self):
        self.assertEqual(self.review.director, "Orson Welles")

    def test_review_actors(self):
        self.assertEqual(self.review.actors, "Orson Welles and Joseph Cotten")

    def test_review_review(self):
        self.assertEqual(
            self.review.review,
            "One of the greatest films of all time, a must see. A true, timeless masterpiece.",
        )

    def test_review_year(self):
        self.assertEqual(self.review.year, 1941)

    def test_review_stars(self):
        self.assertEqual(self.review.stars, "ssss")

    def test_url_pattern(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(
            response,
            "One of the greatest films of all time, a must see. A true, timeless masterpiece.",
        )
