import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phrase(self):
        translator = PigLatin.PigLatin('This is a phrase')
        self.assertEqual(translator.get_phrase(),'This is a phrase')

    def test_empty_str_nil(self):
        translator = PigLatin.PigLatin('')
        self.assertEqual(translator.translate(),'nil')