def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()


def check_winner(board, symbol):
    for row in board:
        if row[0] == row[1] == row[2] == symbol:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


def is_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def get_move(player, board):
    while True:
        try:
            move = int(input(player + ", choose a position (1-9): ")) - 1
            row = move // 3
            col = move % 3
            if 0 <= move < 9 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid or taken spot. Try again.")
        except:
            print("Please enter a valid number.")


def use_special_move(board, enemy_symbol):
    while True:
        try:
            move = int(input("Choose a cell to erase your opponent's symbol (1-9): ")) - 1
            row = move // 3
            col = move % 3
            if 0 <= move < 9 and board[row][col] == enemy_symbol:
                board[row][col] = " "
                print("✔ Opponent's symbol removed!")
                return
            else:
                print("You can only remove your opponent’s symbol.")
        except:
            print("Please enter a valid number.")


def main():
    print("Welcome to Tic-Tac-Toe with a One-Time Special Move!")

    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")
    s1 = input(p1 + ", choose your symbol: ")
    s2 = input(p2 + ", choose a different symbol: ")
    while s1 == s2:
        s2 = input("Symbol already taken. Choose another: ")

    board = [[" " for _ in range(3)] for _ in range(3)]
    p1_used = False
    p2_used = False
    turn = 1

    print_board(board)

    while True:
        if turn % 2 == 1:
            player = p1
            symbol = s1
            enemy_symbol = s2
            used = p1_used
        else:
            player = p2
            symbol = s2
            enemy_symbol = s1
            used = p2_used

        # Ask if player wants to use special move
        if not used:
            use = input(player + ", do you want to use your special move? (y/n): ")
            if use.lower() == "y":
                use_special_move(board, enemy_symbol)
                if turn % 2 == 1:
                    p1_used = True
                else:
                    p2_used = True
                print_board(board)

        # Normal move
        row, col = get_move(player, board)
        board[row][col] = symbol
        print_board(board)

        if check_winner(board, symbol):
            print("🎉 Congratulations, " + player + " wins!")
            break
        elif is_draw(board):
            print("🤝 It's a draw.")
            break

        turn += 1


if _name_ == "_main_":
    main()