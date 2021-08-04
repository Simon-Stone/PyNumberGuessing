import random


# **********************************************************************************************************************
# **********************************************************************************************************************


class GameManager:
    """
    Manages the game. Think of it as the game's "Start Menu".
    """
    def __init__(self, lowest=1, highest=100):
        print("****************************************************")
        print("********** Welcome to Guess the Number! ************")
        print("****************************************************")
        self.lowest = lowest
        self.highest = highest

    def new_game(self):
        GuessTheNumber(self.lowest, self.highest).play()

    def options(self):
        selection = 0
        while selection != 3:
            print("(1) Change lowest possible number")
            print("(2) Change highest possible number")
            print("(3) Return to main menu")
            selection = int(input("> "))
            choices = {1: self.set_lowest, 2: self.set_highest}
            if selection < 3:
                choices[selection]()
        self.print_menu()

    def print_menu(self):
        print("(1) New Game")
        print("(2) Options")
        print("(3) Quit")
        selection = int(input("> "))
        choices = {1: self.new_game, 2: self.options, 3: self.quit}
        choices[selection]()

    def quit(self):
        print("Thanks for playing!")

    def run(self):
        self.print_menu()

    def set_lowest(self):
        self.lowest = int(input("Set the lowest possible number: "))

    def set_highest(self):
        self.highest = int(input("Set the highest possible number: "))

# **********************************************************************************************************************
# **********************************************************************************************************************

class GuessTheNumber:
    """
    A number guessing game
    """
    def __init__(self, a: int, b: int):
        """
        Initialize the game
        :param a: Lowest possible number
        :param b: Highest possible number
        """
        self.lowest = a
        self.highest = b
        self.the_number = random.randint(a, b)
        self.hints = list()
        self.generate_hints()
        self.guess_correct = False
        self.current_score = 100

    def generate_hints(self):
        """
        Generate a list of hints
        """
        self.hints = list()
        for divider in range(2, 10):
            if self.the_number % divider == 0:
                self.hints.append(f"The secret number is a multiple of {divider}!")

    def give_hint(self, guess):
        """
        Give a random hint
        """
        x = random.randint(0, 1)
        if x and len(self.hints) > 0:
            return self.hints.pop(random.randrange(len(self.hints)))
        else:
            if guess > self.the_number:
                return "You guessed too high!"
            elif guess < self.the_number:
                return "You guessed too low!"

    def process_guess(self, guess: int):
        """
        Process the guessed number and give a hint if necessary
        """
        x = self.the_number
        if guess == x:
            print("Congratulations! That's my number!")
            self.guess_correct = True
            return
        print("Wrong!")
        print(self.give_hint(guess))
        self.current_score -= 1

    def play(self):
        while not self.guess_correct:
            print(f"Your current score is {self.current_score}.")
            print(f"Guess a number between {self.lowest} and {self.highest}!")
            guess = int(input("> "))
            self.process_guess(guess)
        print(f"Your final score: {self.current_score}")


# **********************************************************************************************************************
# **********************************************************************************************************************


if __name__ == '__main__':
    GameManager().run()
