# lib/helpers.py
from models.card_type import Card_type
from models.card import Card

def list_card_types():
    types = Card_type.get_all()
    for type in types:
        print(type.name)

def list_cards():
    cards = Card.get_all()
    for card in cards:
        print(f"Name: ", {card.name}, "Type: ", {card.type}, "ID: ", {card.id})

def find_card_by_name():
    name = input("Enter Card Name: ")
    card = Card.find_by_name(name)
    print(
        f"Name: ", {card.name}, "Type: ", {card.type}, "ID: ", {card.id}
    ) if card else print("Card not found.")

def find_card_type_by_name():
    type = input("Enter Card Type: ")
    card = Card_type.find_by_name(type)
    print(type) if type else print("Card Type not found.")

def list_cards_of_type():
    type = input("Enter Card Type: ")
    cards = Card.get_all()
    [print(card.name) for card in cards if card.type == type]
    
def create_new_card():
    name = input("Enter Name for your new card: ")
    type = input("Enter Type of your new card: ")
    new_card = Card.create(name, type)
    print(f"New card created: {new_card.name} {new_card.type} {new_card.id}", )

def create_new_card_type():
    name = input("Enter the name of your new card type: ")
    new_card_type = Card_type.create(name)
    print(f"New card type created: {new_card_type.name}")

def exit_program():
    print("Goodbye!")
    exit()