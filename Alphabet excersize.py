import string
class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print('Буквы алфавита: ',self.letters)

    def letters_num(self):
        print('N of letters: ', len(self.letters))
        return len(self.letters)

class EngAlphabet(Alphabet):
    default_lang = 'En'
    default_letters = string.ascii_lowercase
    __letters_num = len(default_letters)

    def __init__(self, lang=default_lang, letters=default_letters):
        super().__init__(lang,letters)

    def is_en_letter(self, letter):
        if letter in self.letters:
            return True
        else:
            return False

    def letters_num(self):
        print('N of letters: ', EngAlphabet.__letters_num)
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print('This is example')

def main():
    eng = Alphabet('rus', 'АБВГД')
    eng.print()
    eng.letters_num()

    eng = EngAlphabet()
    eng.print()
    eng.letters_num()
    print(eng.is_en_letter('f'))
    print(eng.is_en_letter('Ш'))
    EngAlphabet.example()
if __name__ == '__main__':
    main()
