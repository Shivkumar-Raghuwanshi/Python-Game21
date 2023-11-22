def play_game21():
    current_number = 0
    while current_number < 21:
        user_number = int(input("Your turn: Enter a number between 1 and 3: "))
        if user_number < 1 or user_number > 3:
            print("invalid input. Please enter the number between 1 and 3")
            continue
        current_number += user_number
        print("Current number is", current_number)
        if current_number >= 21:
            print("You lose!")
            break
        computer_number = 4 - user_number
        current_number += computer_number
        print("Computer's turn: Computer adds", computer_number)
        print("Current number is", current_number)
        if current_number >= 21:
            print("You win!")


play_game21()
