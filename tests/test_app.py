import unittest

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index_page_renders_photo_gallery(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("photo-gallery", html)
        self.assertIn("holy-harvest-ministries.jpeg", html)
        self.assertIn("photo-caption", html)
        self.assertIn("holy harvest ministries", html.lower())
        self.assertIn("lightbox", html)

    def test_photo_route_serves_image(self):
        response = self.client.get("/photos/holy-harvest-ministries.jpeg")
        self.assertEqual(response.status_code, 200)
        self.assertIn("image/", response.content_type)


if __name__ == "__main__":
    unittest.main()
