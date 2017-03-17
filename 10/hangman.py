from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman:
    def __init__(self,word):
        self.word = word
        self.letters = []

    def get_word_to_show(self):
        return re.sub('['+"".join(ASCII)+']',PLACEHOLDER,self.word)

    def game_over(self):
        return len(HANG_GRAPHICS)==0

    def game_win(self):
        return self.get_word_to_show() == self.word

    def manage_letter(self, letter):
        if letter in ASCII:
            if letter not in self.word:
                print(HANG_GRAPHICS.pop(0)+'\n\n')
            self.letters.append(letter)
            ASCII.pop(ASCII.index(letter))
        elif letter in self.letters:
            print('{} already picked\n'.format(letter))
        else:
            print('This character is not valid\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    h = Hangman(word)
    while not h.game_over() and not h.game_win():
        print(h.get_word_to_show())
        letter = input('Pick a letter ')
        h.manage_letter(letter)
    if h.game_over():    
        print('Dead! Answer was: {}'.format(h.word))
    else:
        print('Congratulation!')
