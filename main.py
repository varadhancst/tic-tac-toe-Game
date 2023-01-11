import random
import time


class Tic_tac_toe:
    row1 = ["⬜️", "⬜️", "⬜️"]
    row2 = ["⬜️", "⬜️", "⬜️"]
    row3 = ["⬜️", "⬜️", "⬜️"]
    tic_tac_map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    user_input = [11, 12, 13, 21, 22, 23, 31, 32, 33]
    empty_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(user_input)
    game_start = True

    while game_start:
        if len(empty_list) <= 5:
            print("The match is draw")
            game_start = False
        else:
            position = int(input("Where do you want to put the treasure? "))
            if position in user_input:
                position = str(position)
                x = int(position[0])
                y = int(position[1])

                if tic_tac_map[x - 1][y - 1] == "⬜️":
                    tic_tac_map[x - 1][y - 1] = " X  "
                    user_input[user_input.index(int(position))] = "X"
                    empty_list.pop()
                    if game_start:
                        print(user_input)
                        print(f"{row1}\n{row2}\n{row3}")
                        print(empty_list)
                        print(len(empty_list))

                    if tic_tac_map[0][0] == " X  " and tic_tac_map[0][1] == " X  " and tic_tac_map[0][2] == " X  ":
                        print("You won the match")
                        game_start = False
                    elif tic_tac_map[1][0] == " X  " and tic_tac_map[1][1] == " X  " and tic_tac_map[1][2] == " X  ":
                        print("You won the match")
                        game_start = False
                    elif tic_tac_map[2][0] == " X  " and tic_tac_map[2][1] == " X  " and tic_tac_map[2][2] == " X  ":
                        print("You won the match")
                        game_start = False
                    elif tic_tac_map[0][0] == " X  " and tic_tac_map[1][0] == " X  " and tic_tac_map[2][0] == " X  ":
                        print("You won the match")
                        game_start = False
                    elif tic_tac_map[0][1] == " X  " and tic_tac_map[1][1] == " X  " and tic_tac_map[2][1] == " X  ":
                        print("You won the match")
                        game_start = False
                    elif tic_tac_map[0][2] == " X  " and tic_tac_map[1][2] == " X  " and tic_tac_map[2][2] == " X  ":
                        print("You won the match")
                        game_start = False
                    # elif treasure_map[0][0] == " X  " and treasure_map[1][1] == " X  " and treasure_map[2][2]
                    # == " X  ": print("You won the match") game_start = False elif treasure_map[2][0] == " X  "
                    # and treasure_map[1][1] == " X  " and treasure_map[0][2] == " X  ": print("You won the
                    # match") game_start = False

                    time.sleep(1)

                    computer_select = True
                    computer_choice = None
                    while computer_select:
                        computer_choice = str(random.choice(user_input))
                        if computer_choice == "X" or computer_choice == "O":
                            computer_choice = str(random.choice(user_input))
                        elif computer_choice != "X" or computer_choice != "O":
                            computer_select = False
                    computer_choice = str(computer_choice)
                    x = int(computer_choice[0])
                    y = int(computer_choice[1])
                    if tic_tac_map[x - 1][y - 1] == "⬜️":
                        tic_tac_map[x - 1][y - 1] = " O  "
                        user_input[user_input.index(int(computer_choice))] = "O"
                        if game_start:
                            print(user_input)
                            print(f"{row1}\n{row2}\n{row3}")

                        if tic_tac_map[0][0] == " O  " and tic_tac_map[0][1] == " O  " and tic_tac_map[0][2] == " O  ":
                            print("You Lose")
                            game_start = False
                        elif tic_tac_map[1][0] == " O  " and tic_tac_map[1][1] == " O  " and tic_tac_map[1][
                            2] == " O  ":
                            print("You Lose")
                            game_start = False
                        elif tic_tac_map[2][0] == " O  " and tic_tac_map[2][1] == " O  " and tic_tac_map[2][
                            2] == " O  ":
                            print("You Lose")
                            game_start = False
                        elif tic_tac_map[0][0] == " O  " and tic_tac_map[1][0] == " O  " and tic_tac_map[2][
                            0] == " O  ":
                            print("You Lose")
                            game_start = False
                        elif tic_tac_map[0][1] == " O  " and tic_tac_map[1][1] == " O  " and tic_tac_map[2][
                            1] == " O  ":
                            print("You Lose")
                            game_start = False
                        elif tic_tac_map[0][2] == " O  " and tic_tac_map[1][2] == " O  " and tic_tac_map[2][
                            2] == " O  ":
                            print("You Lose")
                            game_start = False
                else:
                    print("you already placed in this place")

            elif position == 0:
                game_start = False
            else:
                print("Invalid input")


Tic_tac_toe()
