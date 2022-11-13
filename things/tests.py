from django.test import TestCase
from things.models import Thing

# Create your tests here.
class ThingsModelTestCase(TestCase):
    def setUp(self):
        self.thing = Thing.objects.create(
            name='John',
            description='The quick brown fox jumps over the lazy frog',
            quantity=6
        )