"""
" " = No Ships (Water)
"o" = Ship
"^" = Water Hit with Bullet
"*" = Ship Hit with Bullet
"  *  "
"-----"
"""
import random

# Global variable for grid size
board_size = 10
# Global variable for grid
my_guessing_board = [(["     "] * board_size) for row in range(board_size)]

computer_guessing_board = [(["     "] * board_size) for row in range(board_size)]

# Global variable for number of ships to place
total_ships = 5
# Global variable for game over
game_over = False
# Global variable for number of ships sunk
player_sunk_ships = 0

computer_sunk_ships = 0
# Global variable for ship positions
# number of ship blocks on grid
player_total_ships = -1
ship_positions = [[]]
ship_positions_grid = [(["     "] * board_size) for row in range(board_size)]

#number of ship blocks on grid
computer_total_ships = -1
computer_positions = [[]]
computer_positions_grid = [(["     "] * board_size) for row in range(board_size)]

number_of_sunk_ships_by_player = 0
number_of_sunk_ships_by_comp = 0

# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Computer


# Computer guesses
def random_choosing():
    global number_of_sunk_ships_by_comp, player_total_ships
    works = False

    x = 0
    y = 0

    while not works:
        x = random.randint(0, board_size - 1)
        y = random.randint(0, board_size - 1)
        if computer_guessing_board[x][y] == "     ":
            works = True

    if ship_positions_grid[x][y] == "  o  ":
        #print("You got a hit!")
        computer_guessing_board[x][y] = "  *  "

        player_total_ships -= 1
    else:
        #print("You missed")
        computer_guessing_board[x][y] = "  ^  "

    pass


# computer places random ships
def random_ship():
    global computer_total_ships

    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    length = random.randint(0, 4)
    ran = random.randint(0, 3)
    direction = ""
    if ran == 0:
        direction = "right"
    elif ran == 1:
        direction = "left"
    elif ran == 2:
        direction = "up"
    elif ran == 3:
        direction = "down"

    trying = try_to_place_ship_on_grid(x, y, direction, length, computer_positions, computer_positions_grid)
    # check if valid location
    while not trying:  # might not run last time
        ran = random.randint(0, 3)
        if ran == 0:
            direction = "right"
        elif ran == 1:
            direction = "left"
        elif ran == 2:
            direction = "up"
        elif ran == 3:
            direction = "down"

        trying = try_to_place_ship_on_grid(x, y, direction, length, computer_positions, computer_positions_grid)

    if computer_total_ships == -1:
        computer_total_ships = length + 1
        #print("starting computer length: " + str(computer_total_ships))
    else:
        computer_total_ships += length + 1
        #print("adding computer length: " + str(computer_total_ships))

    return trying


# choose where to place your ships
def choosing_ships():
    global player_total_ships
    for i in range(total_ships):
        works = False
        while works is False:
            print("Making ship " + str(i + 1) + " : ")
            x = int(input("Which row would you like to place your ship? (as numbers): "))
            y = int(input("Which column would you like to place your ship? (as numbers): "))
            length = int(input("How long would you like your ship? (Choose 1-3): "))
            if length >= 4 or length <= 0:
                print("The length is changed to 2")
                length = 2
            length -= 1
            x -= 1
            y -= 1
            direction = input("'right', 'left', 'up', or 'down': ")

            trying = try_to_place_ship_on_grid(x, y, direction, length, ship_positions, ship_positions_grid)

            print("printing Your ship position grid: ")
            print_grid(ship_positions_grid)

            if trying:
                works = True
                if player_total_ships == -1:
                    player_total_ships = length + 1
                    #print("starting player length: " + str(player_total_ships))
                else:
                    player_total_ships += length + 1
                    #print("adding player length: " + str(player_total_ships))
            else:
                print("You cannot place a ship there")

    pass


def fill_computer_positions():
    # choose 5 ships for computer_positions and computer_position_grid

    for i in range(total_ships):
        random_ship()

    pass


# adds valid ships to grid
def validate_grid_and_place_ship(start_row, end_row, start_col, end_col, p, p_grid):
    row_length = end_row - start_row
    col_length = end_col - start_col

    for i in range(row_length):
        for n in range(col_length):
            if p_grid[n][i] == "  o  ":
                return False

    #print(str(start_row) + " " + str(end_row) + " " + str(start_col) + " " + str(end_col))
    # add ship if ship_positions only equal to "     "
    p.append([start_row, end_row, start_col, end_col])
    for i in range(start_row, end_row):
        for n in range(start_col, end_col):
            p_grid[n][i] = "  o  "
            # print(str(i) + " " + str(n))
            # print_grid(ship_positions_grid)

    return True


# test the given positions
def try_to_place_ship_on_grid(row, col, direction, length: int, p, p_grid):
    global board_size

    start_row = row
    end_row = row + 1
    start_col = col
    end_col = col + 1

    if direction == "left":
        if start_row - length < 0:
            return False
        start_row -= length
    elif direction == "right":
        if end_row + length >= board_size:
            return False
        end_row += length
    elif direction == "up":
        if start_col - length < 0:
            return False
        start_col -= length
    elif direction == "down":
        if end_col + length >= board_size:
            return False
        end_col += length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col, p, p_grid)


def create_grid():
    global my_guessing_board
    global board_size
    global total_ships
    global ship_positions

    pass

    try_to_place_ship_on_grid(0, 0, 0, 0)


def print_grid(board_list):
    global alphabet

    print("  ", end="")
    for i in range(board_size):
        print("  " + alphabet[i] + "   ", end="")
    print("")
    for i in range(board_size):
        print(i + 1, end="")
        if i <= 8:
            print(" ", end="")
        for n in range(board_size):
            print(board_list[i][n], end="")
            if n != board_size - 1:
                print("|", end="")
        print("\n  ", end="")
        if i != board_size - 1:
            for n in range(board_size):
                if n != board_size - 1:
                    print("------", end="")
                else:
                    print("-----")

    pass


# Player chooses shooting position
def accept_valid_bullet_placement(positions):
    global alphabet, number_of_sunk_ships_by_player
    global my_guessing_board, computer_total_ships

    works = False
    x = 0
    y = 0

    while not works:
        y = int(input("Which row? (as numbers): ")) - 1
        x = int(input("Which column? (as numbers): ")) - 1

        if 0 <= x < board_size:
            if 0 <= y < board_size:
                if positions[x][y] == "     ":
                    works = True

    # Add to computer list
    if computer_positions_grid[x][y] == "  o  ":
        print("You got a hit!")
        my_guessing_board[x][y] = "  *  "

        computer_total_ships -= 1
    else:
        print("You missed")
        my_guessing_board[x][y] = "  ^  "

    return x, y



def check_for_ship_sunk(row, col, p, p_grid):
    global my_guessing_board

    for position in p:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if p_grid[r][c] != "  *  ":
                        return True
    return False


def shoot_bullet(positions):
    global my_guessing_board
    global number_of_sunk_ships_by_player

    row, col = accept_valid_bullet_placement(positions)

    if computer_positions_grid[row][col] == "  o  ":
        print("You got a hit!")
        my_guessing_board[row][col] = "  *  "

        if check_for_ship_sunk(row, col, computer_positions, computer_positions_grid):
            number_of_sunk_ships_by_player += 1
    else:
        print("You missed")
        my_guessing_board[row][col] = "  ^  "

    pass


def check_for_game_over():
    global number_of_sunk_ships_by_player, player_total_ships
    global number_of_sunk_ships_by_comp, computer_total_ships
    global total_ships
    global game_over

    if computer_total_ships == 0:
        print("You won! Congrats!")
        game_over = True
    elif player_total_ships == 0:
        print("The computer won! You lost. D: Better luck next time. ")
        game_over = True

    pass


def main():
    global game_over

    chose_ship_placement = False

    print("Let's play Battle Ship!")
    print("Can you beat the computer?")
    print("Place your ships and guess where your opponent's ships are")

    print(ship_positions_grid)
    print_grid(ship_positions_grid)

    while game_over is False:
        if chose_ship_placement is False:
            # chose where to place all 5 ships
            # print_grid(ship_positions_grid)

            choosing_ships()
            fill_computer_positions()
            #print_grid(computer_positions_grid)

            chose_ship_placement = True

        else:
            # print guessing grid
            print("Printing your guessing board")
            print_grid(my_guessing_board)
            # you choose where to shoot
            accept_valid_bullet_placement(my_guessing_board)
            # check what you shot
            print("Printing your guessing board")
            print_grid(my_guessing_board)
            # computer's turn to shoot
            random_choosing()
            # check what the computer shot
            print("Printing computer guessing board")
            print_grid(computer_guessing_board)

            # check if game is over
            check_for_game_over()

    pass
# add computer_total_ships and player_total_ships in program
# they should add up all the added ships

if __name__ == '__main__':
    main()
