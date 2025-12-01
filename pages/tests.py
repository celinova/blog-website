from django.test import TestCase
from django.utils import timezone
from .models import Entry

# ----------------------------------------------------------------------
# UNIT TESTS
# ----------------------------------------------------------------------


class PageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.entry = Entry.objects.create(
            entry_title="test", entry_text="lorem ipsum", publish_date=timezone.now()
        )

    def test_check_existing_object(self):
        self.assertEqual(self.entry.entry_title, "test")
        self.assertEqual(self.entry.entry_text, "lorem ipsum")
