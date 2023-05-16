import random

def get_valid_number_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except :
            print('Invalid input. Please enter a number.')

def calculate_bacteria():
    init_bacteria = get_valid_number_input('Enter initial count of bacteria: ')
    num_hours = get_valid_number_input('Enter the number of hours: ')

    hour = 60
    minute = 20

    No = init_bacteria
    time_N = int(num_hours * hour / minute)

    print('The number of bacteria per hour will be:')

    for i in range(No):
        # Calculate movement for each bacteria
        movement = random.randint(-1, 1)
        new_count = (i + 1 + movement) * (num_hours / time_N)
        print('Hour ' + str(i + 1) + ' = ' + str(int(new_count)))

                # Add line of bacteria moving
        if movement == -1:
            print(f"Bacteria {i+1} moved left.")
        elif movement == 0:
            print(f"Bacteria {i+1} stayed in place.")
        elif movement == 1:
            print(f"Bacteria {i+1} moved right.")


def restart_program():
    while True:
        print('\nDo you want to restart? (Y/N)')
        restart_input = input().upper()

        if restart_input == 'Y':
            calculate_bacteria()
        elif restart_input == 'N':
            break
        else:
            print('Invalid input. Please enter Y or N.')

calculate_bacteria()
restart_program()
