import random

words = ["apple", "python", "game", "mobile", "laptop"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")
print("You have 6 chances to guess the correct word.")


while attempts > 0:
    
    display_word = ""
    for char in word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
    elif guess in word:
        print("Good guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        attempts -= 1
        guessed_letters.append(guess)
        print("Attempts left:", attempts)


if attempts == 0:
    print("\n Game Over!")
    print("The correct word was:", word)