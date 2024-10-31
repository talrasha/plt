import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phrase(self):
        translator = PigLatin('This is a phrase')
        self.assertEqual(translator.get_phrase(),'This is a phrase')

    def test_empty_str_nil(self):
        translator = PigLatin('')
        self.assertEqual(translator.translate(),'nil')

    def test_start_vowel_end_y(self):
        translator = PigLatin('any')
        self.assertEqual(translator.translate(),'anynay')

    def test_start_vowel_end_consonant(self):
        translator = PigLatin('ask')
        self.assertEqual(translator.translate(),'askay')

    def test_start_vowel_end_vowel(self):
        translator = PigLatin('apple')
        self.assertEqual(translator.translate(),'appleyay')

    def test_start_consonant(self):
        translator = PigLatin('hello')
        self.assertEqual(translator.translate(),'ellohay')

    def test_start_mult_consonants(self):
        translator = PigLatin('known')
        self.assertEqual(translator.translate(),'ownknay')

    def test_multiple_words(self):
        translator = PigLatin('hello world')
        self.assertEqual(translator.translate(),'ellohay orldway')

    def test_composite_words(self):
        translator = PigLatin('well-being')
        self.assertEqual(translator.translate(),'ellway-eingbay')

    # .,;:'?!()
    def test_punctuation(self):
        translator = PigLatin("hello world!")
        self.assertEqual(translator.translate(),"ellohay orldway!")

    def test_parenthesis(self):
        translator = PigLatin("(hello world)")
        self.assertEqual(translator.translate(),"(ellohay orldway)")

    def test_punctuation_2(self):
        translator = PigLatin("hello world, nice day.")
        self.assertEqual(translator.translate(),"ellohay orldway, icenay ayday.")

    def test_punctuation_3(self):
        translator = PigLatin("hello world; it's a nice day:")
        self.assertEqual(translator.translate(),"ellohay orldway; it'say ayay icenay ayday:")

    def test_punctuation_between(self):
        translator = PigLatin("hello world! how are you?")
        self.assertEqual(translator.translate(),"ellohay orldway! owhay areyay ouyay?")

    def test_unallowed_punctuation(self):
        translator = PigLatin('test% and€')
        self.assertRaises(PigLatinError,translator.translate)

    def test_uppercase(self):
        translator = PigLatin('HELLO')
        self.assertEqual(translator.translate(),'ELLOHAY')

    def test_uppercase_initial(self):
        translator = PigLatin('Hello World!')
        self.assertEqual(translator.translate(),'Ellohay Orldway!')
