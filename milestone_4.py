mylist = ["blue", "car", 'horse', 'titanium', 'composite']

def check_guess(): 
    import random
    random.choice(mylist)
    word = random.choice(mylist)
    print(f'{word} is the radom word in question')

    guess = (input('Please, enter a single alphabetical character: ')).lower()
    while guess == guess in word:
        if len(guess) == 0:
            guess = input('Please, enter a single alphabetical character: ').lower()
        elif (len(guess) == 1) and guess.isalpha() == True:
            print(f'Good guess! {guess} is in {word}.')
            break    # this controls the loop depending on indent
    else:
        print(f'Sorry, {guess} is not in {word}. Try again.')
check_guess()