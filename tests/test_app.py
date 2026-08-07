import unittest

from App import build_page


class AppPageTests(unittest.TestCase):
    def test_alarm_page_contains_customizable_reminder_controls(self):
        page = build_page("/alarms")

        self.assertIn("Stretch reminder", page)
        self.assertIn("Start reminder", page)
        self.assertIn("hours", page)
        self.assertIn("Daily", page)
        self.assertIn("Every other day", page)
        self.assertIn("Every week", page)
        self.assertIn("Notification title", page)
        self.assertIn("Soft sound", page)
        self.assertIn("Stop reminder", page)

    def test_stretches_page_contains_tailored_suggestions_and_ratings(self):
        page = build_page("/stretches")

        self.assertIn("Stretch suggestions", page)
        self.assertIn("Tailor this list to your preferences", page)
        self.assertIn("Rate this stretch", page)
        self.assertIn("Gentle", page)
        self.assertIn("Shoulder rolls", page)

    def test_stretches_page_persists_reviews_with_browser_storage(self):
        page = build_page("/stretches")

        self.assertIn("localStorage", page)
        self.assertIn("setItem", page)
        self.assertIn("getItem", page)


if __name__ == "__main__":
    unittest.main()
