vocab=["bookish", "napkin", "crocodile", "hurricane"]
import random
q=random.randint(0,3)
z=vocab[q]
def hangman(word):
    wrong=0
    stages=["",
    "________     ",
    "|       |    ",
    "|       |    ",
    "|       O    ",
    "|      /|\   ",
    "|      / \   ",
    "|            "]
    rletters=list(word)
    board=["__"]*len(word)
    win=False
    print("You are welcome!")
    #
    while wrong<len(stages)-1:
        print("\n")
        msg="Enter a letter: "
        guess=input(msg)
        if guess in rletters:
            cind=rletters.index(guess)
            board[cind]=guess
            rletters[cind]='$'
        else:
            wrong+=1
        print((" ".join(board)))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You won! The word was: ")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lost! The word was: {}.".format(word))
hangman(z)