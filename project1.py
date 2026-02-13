import random

def play_word_game():
    words = ["soccer", "basketball", "baseball", "football", "hockey", "sailing", "skating", "rugby", "running"]
    word = random.choice(words)
    hint = "_"*len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to the Sport Guessing Game!")

    while attempts > 0 and "_" in hint:
        print(f"\nWord: {hint}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            new_hint = ""
            for i in range(len(word)):
                if word[i] == guess:
                    new_hint += guess
                else:
                    new_hint += hint[i]
            hint = new_hint
        else:
            print("Wrong guess.")
            attempts -= 1
    if "_" not in hint:
        print(f"\nCongratulations! You guessed the word: {word}")
    else: 
        print(f"\nGame Over! The word was: {word}")

play_word_game()

