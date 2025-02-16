from django.test import TestCase


# Create your tests here.


class FictiveTest(TestCase):
    def test_fictive(self):
        self.assertEqual(1, 1)

    def test_fail(self):
        self.assertEqual(1, 2)
