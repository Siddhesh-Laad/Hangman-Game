import random

def hangman():
    list_of_words = ['Hangman', 'Gaming', 'Function', 'Python', 'Programming', 'CodeMaster', 'Logic', 'Word', 'Syntax']
    word = random.choice(list_of_words).upper()
    turns = 10
    guessmade = set()
    valid_entry = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    print("Guess the word:", '_ ' * len(word))

    while turns > 0:
        main_word = ""
        
        for letter in word:
            if letter in guessmade:
                main_word += letter + ' '
            else:
                main_word += "_ "

        if main_word.strip() == ' '.join(word):
            print(main_word)
            print("You Won !!!!")
            break
        
        print("Current word:", main_word)
        guess = input("Enter your guess: ").upper()

        if len(guess) != 1 or guess not in valid_entry:
            print("Enter a valid character (a single letter).")
            continue

        if guess in guessmade:
            print("You already guessed that letter.")
            continue

        guessmade.add(guess)
        
        if guess not in word:
            turns -= 1
            print(f"Wrong guess. {turns} turns left.")
            print_hangman(turns)
            
            if turns == 0:
                print("You lose! The word was:", word)
                print_hangman(turns)
                break
        else:
            print("Good guess!")

def print_hangman(turns):
    stages = [
        "         O\n        /|\\ \n        / \\",
        "         O\n        /|\\ \n        / ",
        "         O\n        /|\\ \n         ",
        "         O\n        /|\\ ",
        "         O\n        /| ",
        "         O\n        / ",
        "         O\n         ",
        "         \n         ",
        "         \n         ",
        "         \n         ",
        "         \n         "
    ]
    print(stages[10 - turns])

if __name__ == "__main__":
    try:
        name = input("ENTER YOUR NAME -> ")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        print(f"Welcome, {name}!")
        print("-----------------------------")
        print("Try to guess the word in less than 10 attempts")
        hangman()
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
