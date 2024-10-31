
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
            if word[0] in 'aeiouAEIOU':
                if word[-1] in 'aeiouAEIOU':
                    translated_words.append(word + 'yay')
                elif word[-1] == 'y':
                    translated_words.append(word + 'nay')
                else:
                    translated_words.append(word + 'ay')
            else:
                translated_words.append(word[1:] + word[0] + 'ay')
        return ' '.join(translated_words)

