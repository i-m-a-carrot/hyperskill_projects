from random import choice
import string
class HangMan:
    def __init__(self):
        self.guess_words = choice(('python','java','kotlin','javascript'))
        self.dashes = list("-" * len(self.guess_words))
        self.store_input = []
        self.count = 8

    def main_board(self):
        while True:
            main_input = input("Type \"play\" to play the game, \"exit\" to quit: ")
            if main_input == "play":
                print("H A N G M A N")
                self.game_logic()
            elif main_input == "exit":
                exit()

    def game_logic(self):
        while self.count > 0:
            print()
            print(self.count)
            print(''.join(self.dashes))
            usr_input = input("Input a letter: ")
            if len(usr_input) > 1:
                print("You should input a single letter")
            elif not usr_input.islower():
                print("Please enter a lowercase English letter")
            elif usr_input in self.store_input:
                    print("You've already guessed this letter")
            else:
                self.check_replace(usr_input)
                if set(self.dashes) == set(self.guess_words):
                    print(self.guess_words)
                    print("You guessed the word!")
                    print("You survived!")
                    break
                if self.count == 0:
                    print("You lost!")
                    break

    def check_validation(self,value):
        if len(value) > 1:
                print("You should input a single letter")
        elif not value.islower():
                print("Please enter a lowercase English letter")


    def check_replace(self,value):
        self.store_input.append(value)
        if value in self.dashes:
            print("You've already guessed this letter")
        elif value not in self.guess_words:
            self.count -= 1
            print("That letter doesn't appear in the word")
        else:
            for n in range(len(self.guess_words)):
                if self.guess_words[n] == value:
                    self.dashes[n] = value
                else:
                    continue

hangMan = HangMan()
hangMan.main_board()

