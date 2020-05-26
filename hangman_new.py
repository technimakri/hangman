import string, random_word
r = random_word.RandomWords()

def check_survived():
    if "-" not in set(hidden_word):
            print("")
            print("".join(hidden_word))
            print("You guessed the word!")
            print("You survived!")
            print("")
            return True

def reveal_letter():
    for count, letter in enumerate(word):
        if letter == guess:
            hidden_word[count] = guess
while True:
    menu_select = input('Type "play" to start a new game, "exit" to quit: ')
    if menu_select == "play":
        guess_remaining = 8
        word = r.get_random_word(minCorpusCount=5, hasDictionaryDef=True, minLength=5)
        hidden_word = list(len(word) * "-")
        guess_record = []
        print("")
        print("H A N G M A N")
        while guess_remaining != 0:
            print("")
            print("".join(hidden_word))
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
                continue
            if guess not in string.ascii_lowercase:
                print("It is not an ASCII lowercase letter")
                continue
            if guess in guess_record:
                print("You already typed this letter")
                continue
            elif guess in set(word):
                reveal_letter()
                if check_survived():
                    break
            else:
                guess_remaining -= 1
                print("No such letter in the word")
            guess_record.append(guess)
        else:
            print("You are hanged!")
            print(f"Word was {word}")
            print("")
    elif menu_select == "exit":
        break
    else:
        continue


