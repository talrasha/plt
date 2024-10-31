
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == '':
            return 'nil'
        words = self.phrase.split()
        translated_words = []
        for word in words:
            parts = word.split('-')
            translated_parts = []
            for part in parts:
                if part[0] in 'aeiouAEIOU':
                    if part[-1] in 'aeiouAEIOU':
                        translated_parts.append(part + 'yay')
                    elif part[-1] == 'y':
                        translated_parts.append(part + 'nay')
                    else:
                        translated_parts.append(part + 'ay')
                else:
                    first_vowel_idx = next((i for i, letter in enumerate(part) if letter in 'aeiouAEIOU'), None)
                    if first_vowel_idx is None or first_vowel_idx == 0:
                        translated_parts.append(part[1:] + part[0] + 'ay')
                    else:
                        translated_parts.append(part[first_vowel_idx:] + part[:first_vowel_idx] + 'ay')
            translated_words.append('-'.join(translated_parts))
        return ' '.join(translated_words)

