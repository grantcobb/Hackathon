board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
while True:
    print("Board")
    for a in range(0, 8):
        for j in range(0, 8):
            print(board[a][j], end=" ")
        print("")
        row = int(input("Row: ")) - 1
        col = int(input("Column: ")) - 1
        if board[row][col] == ".":
            print("There is no piece there.")
            break
        else:
            piece = board[row][col]
            board[row][col] = "."
            row = int(input("Row: ")) - 1
            col = int(input("Column: ")) - 1
            board[row][col] = piece
