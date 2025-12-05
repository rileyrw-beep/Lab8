from pakudex import Pakudex

def print_introduction():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            max_capacity = int(input("Enter max capacity of the Pakudex: "))
        except ValueError:
            print("Please enter a valid size.")
        else:
            if (max_capacity < 0):
                print("Please enter a valid size.")
            else:
                break
    print(f"The Pakudex can hold {max_capacity} species of Pakuri.")
    print("")

    print("Pakudex Main Menu")
    print("-----------------")
    return max_capacity

def print_menu():
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")
    print()

def print_pakudex(p):
    if p.get_size() == 0:
        print("No Pakuri in Pakudex yet!")
        return
    print("Pakuri In Pakudex:")
    for index, species in enumerate(p.get_species_array()):
        print(f"{index + 1}. {species}")

def show_pakuri(p):
    desired_pakuri = input("Enter the name of the species to display: ")
    stat_list = p.get_stats(desired_pakuri)
    if stat_list is None:
        print("Error: No such Pakuri!")
        return
    print()
    print(f"Species: {desired_pakuri}")
    print(f"Attack: {stat_list[0]}")
    print(f"Defense: {stat_list[1]}")
    print(f"Speed: {stat_list[2]}")

def add_pakuri(p):
    desired_pakuri = input("Enter the name of the species to add: ")
    if p.add_pakuri(desired_pakuri):
        print(f"Pakuri species {desired_pakuri} successfully added!")
    elif p.get_size() == p.get_capacity():
        print("Error: Pakudex is full!")
    else:
        print("Error: Pakudex already contains this species!")

def evolve_pakuri(p):
    desired_pakuri = input("Enter the name of the species to evolve: ")
    if p.evolve_species(desired_pakuri):
        print(f"{desired_pakuri} has evolved!")
    else:
        print("Error: No such Pakuri!")

def main():
    max = print_introduction()
    p = Pakudex(capacity=max)

    #the game loop:
    while True:
        print_menu()
        while True:
            try:
                choice = int(input("What would you like to do? "))
            except ValueError:
                print("Unrecognized menu selection!")
            else:
                if (choice >= 1 and choice <= 6):
                    break
                else:
                    print("Unrecognized menu selection!")


        match choice:
            case 1:
                print_pakudex(p)
                print()
            case 2:
                show_pakuri(p)
                print()
            case 3:
                add_pakuri(p)
                print()
            case 4:
                evolve_pakuri(p)
                print()
            case 5:
                p.sort_pakuri()
                print("Pakuri have been sorted!")
                print()
            case 6:
                print("Thanks for using Pakudex! Bye!")
                break


if __name__ == '__main__':
    main()



"""

    while True:
        user_input = input("Enter a value (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Exiting the program.")
            break  # Exit the loop if the user types 'quit'
        else:
            print(f"You entered: {user_input}")
            # You can perform other operations with user_input here


"""