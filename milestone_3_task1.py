while True:
    guess = input('Please, enter a single alphabetical character :')
    if guess.isalpha() == True and len(guess) == 1 and guess != int:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")