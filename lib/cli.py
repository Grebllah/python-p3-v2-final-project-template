# lib/cli.py

from helpers import (
    exit_program,
    list_card_types,
    list_cards,
    find_card_by_name,
    list_cards_of_type,
    create_new_card,
    create_new_card_type
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_cards()
        elif choice == "2":
            list_card_types()
        elif choice == "3":
            find_card_by_name()
        elif choice == "4":
            list_cards_of_type()
        elif choice == "5":
            create_new_card()
        elif choice == "6":
            create_new_card_type()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all cards")
    print("2. List all card types")
    print("3. Find card by name")
    print("4. List cards by card type")
    print("5. Create a new card")
    print("6. Create a new card type")
    


if __name__ == "__main__":
    main()
