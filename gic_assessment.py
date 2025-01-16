def get_field_dimensions():
    while True:
        try:
            dimensions = input("Enter the width and height of the field: ")
            width, height = map(int, dimensions.split())
            if width > 0 and height > 0:
                return width, height
            else:
                print("Field dimensions must be positive integers. Please try again.")
        except ValueError:
            print("Invalid input. Please enter two positive integers separated by a space.")

def rotate_left(direction):
    directions = ['N', 'W', 'S', 'E']
    index = directions.index(direction)  # Find current direction's index
    return directions[(index + 1) % 4]  # Rotate left (counterclockwise)

def rotate_right(direction):
    directions = ['N', 'E', 'S', 'W']
    index = directions.index(direction)  # Find current direction's index
    return directions[(index + 1) % 4]  # Rotate right (clockwise)

def move_forward(x, y, direction, field_width, field_height):
    if direction == 'N' and y + 1 < field_height:  # Move up (North)
        y += 1
    elif direction == 'E' and x + 1 < field_width:  # Move right (East)
        x += 1
    elif direction == 'S' and y - 1 >= 0:  # Move down (South)
        y -= 1
    elif direction == 'W' and x - 1 >= 0:  # Move left (West)
        x -= 1
    return x, y

def process_commands(car, commands, field_width, field_height):
    x, y, direction = car
    for command in commands:
        if command == 'L':  # Rotate left
            direction = rotate_left(direction)
        elif command == 'R':  # Rotate right
            direction = rotate_right(direction)
        elif command == 'F':  # Move forward
            x, y = move_forward(x, y, direction, field_width, field_height)
    return x, y, direction

# Scenario 1
def main():
    while True:

        print("Welcome to Auto Driving Car Simulation!")

        field_width, field_height = get_field_dimensions()
        print("You have created a field of", field_width, "x", field_height)

        cars = []
        while True:
            if not cars:
                print("\nThere are no cars to drive.")
                print("[1] Add a car to field")
                choice = input("Choose an option: ")
                if choice == '1':
                    name = input("Enter car name: ")
                    while True:
                        try:
                            x, y, direction = input(f"Enter the initial position of {name} (x y Direction): ").split()
                            x, y = int(x), int(y)
                            if direction in ['N', 'E', 'S', 'W'] and 0 <= x < field_width and 0 <= y < field_height:
                                break
                            else:
                                print(
                                    "Invalid position or direction. Ensure x and y are within bounds and direction is N, E, S, or W.")
                        except ValueError:
                            print("Invalid input. Please enter x, y as integers and direction as N, E, S, or W.")
                    while True:
                        try:
                            commands = input(f"Enter the commands for {name}: ").upper()
                            if all(char in ['L', 'R', 'F'] for char in commands):
                                break
                            else:
                                print("Invalid commands. Please enter L or R or F only.")
                        except ValueError:
                            print("Invalid input. Please enter L or R or F only.")
                    cars.append((name, x, y, direction, commands))
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("\n[1] Add a car to field")
                print("[2] Run simulation")
                choice = input("Choose an option: ")
                if choice == '1':
                    name = input("Enter car name: ")

                    while True:
                        try:
                            x, y, direction = input(f"Enter the initial position of {name} (x y Direction): ").split()
                            x, y = int(x), int(y)
                            if direction in ['N', 'E', 'S', 'W'] and 0 <= x < field_width and 0 <= y < field_height:
                                break
                            else:
                                print(
                                    "Invalid position or direction. Ensure x and y are within bounds and direction is N, E, S, or W.")
                        except ValueError:
                            print("Invalid input. Please enter x, y as integers and direction as N, E, S, or W.")
                    while True:
                        try:
                            commands = input(f"Enter the commands for {name}: ").upper()
                            if all(char in ['L', 'R', 'F'] for char in commands):
                                break
                            else:
                                print("Invalid commands. Please enter L or R or F only.")
                        except ValueError:
                            print("Invalid input. Please enter L or R or F only.")

                    cars.append((name, x, y, direction, commands))
                elif choice == '2':
                    print("\nRunning simulation...")
                    results = []
                    for car in cars:
                        name, x, y, direction, commands = car
                        x, y, direction = process_commands((x, y, direction), commands, field_width, field_height)
                        results.append((name, x, y, direction))
                    for result in results:
                        name, x, y, direction = result
                        print(f"- {name} ended at ({x}, {y}) facing {direction}")
                    break
                else:
                    print("Invalid choice. Please try again.")

        while True:
            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                break
            elif choice == '2':
                print("Thank you for running the simulation. Goodbye!")
                return
            else:
                print("Invalid input. Please enter 1 or 2.")


main()