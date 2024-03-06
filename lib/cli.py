# lib/cli.py

from helpers import (
    exit_program,
    list_card_types,
    list_cards,
    find_card_by_name,
    list_cards_of_type,
    list_cards_of_ability,
    create_new_card,
    create_new_card_type,
    delete_card
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
            list_cards_of_ability()
        elif choice == "6":
            create_new_card()
        elif choice == "7":
            create_new_card_type()
        elif choice == "8":
            delete_card()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all cards")
    print("2. List all card types")
    print("3. Find card by name")
    print("4. List cards by card type")
    print("5. List cards by card ability")
    print("6. Create a new card")
    print("7. Create a new card type")
    print("8. Delete a Card")
    


if __name__ == "__main__":
    main()
