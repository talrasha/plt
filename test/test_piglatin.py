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

    def test_start_vowel_end_y(self):
        translator = PigLatin.PigLatin('any')
        self.assertEqual(translator.translate(),'anynay')

    def test_start_vowel_end_consonant(self):
        translator = PigLatin.PigLatin('ask')
        self.assertEqual(translator.translate(),'askay')

    def test_start_vowel_end_vowel(self):
        translator = PigLatin.PigLatin('apple')
        self.assertEqual(translator.translate(),'appleyay')