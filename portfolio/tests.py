from django.test import TestCase
from django.test import TestCase
from .models import Poll


class PollModelTest(TestCase):
    def test_poll_title(self):
        poll = Poll.objects.create(title="Улюблена мова програмування?")
        self.assertEqual(poll.title, "Улюблена мова програмування?")


# Create your tests here.
