'''Rev 3.2 - Check whether the letter guessed by the user is in the secret word that was 
randomly chosen by the computer'''
mylist = ["blue", "car", 'horse', 'titanium', 'composite']
import random
random.choice(mylist)
word = random.choice(mylist)
print(f'{word} is the radom word in question')

guess = input('Please, enter a single alphabetical character: ')
while guess == guess in word:
    if len(guess) == 0:
        guess = input('Please, enter a single alphabetical character: ')
    elif (len(guess) == 1) and guess.isalpha() == True:
        print(f'Good guess! {guess} is in {word}.')
        break    
else:
    print(f'Sorry, {guess} is not in {word}. Try again.')
    