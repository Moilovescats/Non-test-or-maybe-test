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


if __name__ == "__main__":
    unittest.main()
