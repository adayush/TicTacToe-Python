def check():
    # horizontal checking
    for x in (1, 4, 7):
        if moves[str(x)] == moves[str(x+1)] == moves[str(x+2)] == player:
            return moves[str(x)]
    
    # vertical checking
    i = 0
    while(i < 3):
        if moves[str(7 + i)] == moves[str(4 + i)] == moves[str(1 + i)]:
            return moves[str(7 + i)]
        i += 1

    # diagonal checking
    if moves['7'] == moves['5'] == moves['3']:
        return moves['7']
    elif moves['1'] == moves['5'] == moves['9']:
        return moves['1']
    
    return ' '

print("———— Welcome to Tic-Tac-Toe made by Us ————\n\n")

# Mapping the number pad to the grid of the game
moves = {'7': " ", '8': " ", '9': " ",
         '4': " ", '5': " ", '6': " ",
         '1': " ", '2': " ", '3': " "}

turns = 0

while turns < 9:
    print(" %c | %c | %c" % (moves['7'], moves['8'], moves['9']))
    print("———|———|———")
    print(" %c | %c | %c" % (moves['4'], moves['5'], moves['6']))
    print("———|———|———")
    print(" %c | %c | %c" % (moves['1'], moves['2'], moves['3']))

    if turns > 3:
        winner = check()
        if winner == 'X' or winner == 'O':
            print("\nGame Over\n" + winner + " is the winner!")
            break

    player = 'X' if (turns%2 == 0) else 'O'

    print(player + "'s turn")
    
    move = input()
    moves[move] = player

    turns += 1

if turns == 9:
    print("It was a Tie. Well Played :D")
