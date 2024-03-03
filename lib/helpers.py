# lib/helpers.py
from models.card_type import Card_type
from models.card import Card

def list_card_types():
    types = Card_type.get_all()
    for type in types:
        print(type)

def list_cards():
    cards = Card.get_all()
    for card in cards:
        print(f'{card.name}, {card.type}')

def find_card_by_name():
    name = input("Enter Card Name: ")
    card = Card.find_by_name(name)
    print(card) if card else print("Card not found.")

def find_card_type_by_name():
    type = input("Enter Card Type: ")
    card = Card_type.find_by_name(type)
    print(type) if type else print(
        "Card Type not found."
    )

def exit_program():
    print("Goodbye!")
    exit()