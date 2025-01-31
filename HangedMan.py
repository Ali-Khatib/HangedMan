import random


def game():
    print("Hello! Welcome to Hangman!")

    mode = int(input("Choose a mode: \n 1. Singleplayer \n 2. Multiplayer\n"))

    hang = [
        "   _____   ",
        "  |     |  ",
        "  |        ",
        "  |        ",
        "  |        ",
        "  |        ",
        "  |        ",
        "__|__      "
    ]

    stages = [
        (2, "  |     0  "),
        (3, "  |     |  "),
        (3, "  |    /|  "),
        (3, "  |    /|\\ "),
        (4, "  |    /   "),
        (4, "  |    / \\ ")
    ]

    words = [
        "EiSei", "Shin", "Ousen", "KyouKai", "RyoFui", "Ten", "XiangYing", "Karyou", "BaiWu", "LiuBang",
        "RiboKu", "Shouheikun", "Kanki", "Moubou", "Kaede", "Renpa", "Arima", "Sukuna", "Mougou", "Mouten",
        "Buccirati", "Giorno", "Ryusuke", "Koyuki", "Takahiro", "Maho", "Chiba", "Eiji", "Saitou", "Kato",
        "Takahashi", "Tomo", "Mereum", "Tsserdenich", "Aizen", "Koyotte", "Legoshi", "Haru", "Louis", "Juno",
        "Jack", "Risuko", "Gosha", "Collie", "Aoba", "Mitsuha", "Grimmjow", "Kenpachi", "Yamamoto", "Garou",
        "Valentine", "Kaneki", "Rize", "Touka", "Amon", "Ishida", "Uta", "Aokiji", "Jotaro", "Dio", "Joseph",
        "Giorno", "Josuke", "Polnareff", "Eren", "Mikasa", "Armin", "Levi", "Erwin", "Reiner", "Yoshikage",
        "Gon", "Killua", "Kurapika", "Leorio", "Hisoka", "Chrollo", "Ichigo", "Rukia", "Renji", "Toshiro",
        "Byakuya", "Orihime", "Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Law", "Robin", "Franky", "Brook",
        "Jinbei", "Jimbei", "Portgas", "Ace", "Sabo", "Kizaru", "Dante", "Vergil", "Isagi", "King", "Barou",
        "Shidou", "Kaku", "Itachi", "Naruto", "Sasuke", "Sakura", "Kakashi", "Madara", "Hashirama", "Nagato",
        "Minato", "Kabuto", "Tsunade", "Konohamaru", "Kisame", "Hidan", "Kakuzu", "Kurama", "Saitama",
        "Genos", "Goku", "Gohan", "Trunks", "Vegeta", "Piccolo", "Yamato", "Karin", "Shunsui", "Johnny",
        "Nagi", "Bachira", "Gabimaru", "Megumi", "Tanjiro", "Nezuko", "Zenitsu", "Inosuke", "Mitsuri",
        "Kanao", "Giyu", "Rengoku", "Muzan", "Tengen", "Obito", "Hanabi", "Hinata", "Shinobu", "Kiba"
    ]

    guesses = 0
    maxwrong = 7
    correct = 0

    if mode == 1:
        word = random.choice(words)
        wordarea = ["_"] * len(word)
        print(wordarea)
        length = len(word)
        print("You have", length, "letters and", maxwrong, "wrong guesses.")

        while guesses < maxwrong:
            for row in hang:
                print(row)

            guess = input("Guess a letter: ").lower()

            if guess in word.lower():
                for i in range(len(word)):
                    if word[i].lower() == guess and wordarea[i].lower() != guess:
                        wordarea[i] = guess
                        correct += 1
                        print("Correct")
                    elif word[i].lower() == guess and wordarea[i].lower() == guess:
                        print("You already said that!")
                print(" ".join(wordarea))
                if "_" not in wordarea:
                    print("You win!")
                    break
            else:
                if guesses < len(stages):
                    index, update = stages[guesses]
                    hang[index] = update
                guesses += 1
                print("Wrong guess. You have", maxwrong - guesses, "guesses left.")

            if guesses == maxwrong:
                print("You lose! The word was:", word)
                game()

    elif mode == 2:
        word = input("Write the word for me: ")
        print("\n" * 60)
        wordarea = ["_"] * len(word)
        print(wordarea)
        length = len(word)
        print("You have", length, "letters and", maxwrong, "wrong guesses.")

        while guesses < maxwrong:
            for row in hang:
                print(row)

            guess = input("Guess a letter: ").lower()

            if guess in word.lower():
                for i in range(len(word)):
                    if word[i].lower() == guess and wordarea[i].lower() != guess:
                        print("Correct")
                        wordarea[i] = guess
                        correct += 1
                    elif word[i].lower() == guess and wordarea[i].lower() == guess:
                        print("You already said that!")
                print(" ".join(wordarea))
                if "_" not in wordarea:
                    print("You win!")
                    break
            else:
                if guesses < len(stages):
                    index, update = stages[guesses]
                    hang[index] = update
                guesses += 1
                print("Wrong guess. You have", maxwrong - guesses, "guesses left.")

            if guesses == maxwrong:
                print("You lose! The word was:", word)
                game()

    else:
        print("Invalid input, please try again")
        game()


game()
