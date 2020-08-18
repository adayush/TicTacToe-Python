print("———— Welcome to Tic-Tac-Toe made by Ayush ————\n\n")

moves = {'7': " ", '8': " ", '9': " ",
         '4': " ", '5': " ", '6': " ",
         '1': " ", '2': " ", '3': " "}

turns = 0

while(turns<9):
    print(" %c | %c | %c" % (moves['7'], moves['8'], moves['9']))
    print("———|———|———")
    print(" %c | %c | %c" % (moves['4'], moves['5'], moves['6']))
    print("———|———|———")
    print(" %c | %c | %c" % (moves['1'], moves['2'], moves['3']))

    player = 'X' if (turns%2 == 0) else 'O'

    print(player + "'s turn")
    
    move = input()
    moves[move] = player

    turns += 1
    print("\n")