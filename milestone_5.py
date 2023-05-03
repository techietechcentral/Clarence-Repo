import random

class Hangman:
    """
    A class representing a game of Hangman.

    Attributes:
    - word_list (list): A list of words to choose from for the game.
    - num_lives (int): The number of lives the player has to guess the word.
    - word (str): The word chosen for the game.
    - word_guessed (list): A list of underscores representing the letters of the word to guess.
    - num_letters (int): The number of unique letters in the word to guess.
    - list_of_guesses (list): A list of letters guessed by the player.

    Methods:
    - __init__(self, word_list, num_lives=5): Initializes the Hangman game with the given word list and number of lives.
    - check_guess(self, guess): Checks if the guessed letter is in the word, updates the word_guessed list if necessary,
      and decrements the number of lives if the guess is incorrect.
    - ask_for_input(self): Prompts the player to enter a letter guess and handles invalid input.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game with the given word list and number of lives.

        Args:
        - word_list (list): A list of words to choose from for the game.
        - num_lives (int): The number of lives the player has to guess the word.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word, updates the word_guessed list if necessary,
        and decrements the number of lives if the guess is incorrect.

        Args:
        - guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Prompts the player to enter a letter guess and handles invalid input.
        """
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break