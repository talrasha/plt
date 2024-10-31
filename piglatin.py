
from error import PigLatinError

class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return 'nil'

        words = self.phrase.split()
        translated_words = []

        for word in words:
            # Handle punctuation
            prefix_punct = ''
            suffix_punct = ''
            core_word = word

            # Extract prefix punctuation
            while core_word and not core_word[0].isalnum():
                if core_word[0] not in [",",".",";",":","'","?","!","(",")"]:
                    raise PigLatinError

                prefix_punct += core_word[0]
                core_word = core_word[1:]

            # Extract suffix punctuation
            while core_word and not core_word[-1].isalnum():
                if core_word[-1] not in [",",".",";",":","'","?","!","(",")"]:
                    raise PigLatinError

                suffix_punct = core_word[-1] + suffix_punct
                core_word = core_word[:-1]

            # Translate the core word
            if core_word:
                translated_word = self.translate_word(core_word)
            else:
                translated_word = ''

            # Reassemble the word with punctuation
            translated_words.append(prefix_punct + translated_word + suffix_punct)

        return ' '.join(translated_words)

    def translate_word(self, word: str) -> str:
        new_word = ''
        if word[0].lower() in 'aeiou':
            if word[-1] in 'aeiou':
                new_word = word + 'yay'
            elif word[-1] == 'y':
                new_word = word + 'nay'
            else:
                new_word = word + 'ay'
        else:
            first_vowel_idx = next((i for i, letter in enumerate(word) if letter.lower() in 'aeiou'), None)
            if first_vowel_idx is None:
                new_word = word + 'ay'
            else:
                new_word = word[first_vowel_idx:] + word[:first_vowel_idx] + 'ay'

        if word.isupper():
            return new_word.upper()
        elif word.istitle():
            return new_word.title()
        else:
            return new_word

