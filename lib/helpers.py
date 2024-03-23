# lib/helpers.py

from models.card_type import Card_type
from models.card import Card
from models.ability import Ability

def list_cards():
    cards = Card.get_all()
    for card in cards:
        print(f"Name: ", {card.name}, "Type: ", {card.type}, "Abilities", {card.ability}, "ID: ", {card.id})

def list_card_types():
    types = Card_type.get_all()
    for type in types:
        print(type.name)

def list_card_abilities():
    abilities = Ability.get_all()
    for ability in abilities:
        print(ability.name)

def list_cards_of_type():
    type = input("Enter Card Type: ")
    cards = Card.get_all()
    [print(card.name) for card in cards if card.type == type]

def list_cards_of_ability():
    ability = input("Enter Card Ability: ")
    cards = Card.get_all()
    [print(card.name) for card in cards if card.ability == ability]

def find_card_by_name():
    name = input("Enter Card Name: ")
    card = Card.find_by_name(name)
    print(
        f"Name: ", {card.name}, "Type: ", {card.type}, "Ability: ", {card.ability}, "ID: ", {card.id}
    ) if card else print("Card not found.")    
    
def find_card_by_id():
    id = input("Enter Card Id: ")
    card = Card.find_by_id(id)
    print(
        f"Name: ", {card.name}, "Type: ", {card.type}, "Ability: ", {card.ability}, "ID: ", {card.id}
    ) if card else print("Card not found.")  

def create_new_card():
    name = input("Enter Name for your new card: ")
    type = input("Enter Type of your new card: ")
    ability = input("Enter Ability: ")
    new_card = Card.create(name, type, ability)
    print(f"New card created: {new_card.name} {new_card.type} {new_card.ability} {new_card.id}", )

def create_new_card_type():
    name = input("Enter the name of your new card type: ")
    new_card_type = Card_type.create(name)
    print(f"New card type created: {new_card_type.name}")

def create_new_card_ability():
    name = input("Enter new ability name: ")
    effect = input("Enter new ability's effect in 1 sentence: ")
    new_card_ability = Ability.create(name, effect)
    print(f"New card ability created: {new_card_ability.name}, {new_card_ability.effect}")

def delete_card():
    id_ = input("Enter the card's id: ")
    if card := Card.find_by_id(id_):
        card.delete()
        print(f'card {id_} deleted')
    else:
        print(f'card {id_} not found')

def delete_card_type():
    id_ = input("Enter the card type's ID: ")
    if card := Card_type.find_by_id(id_):
        card.delete()
        print(f'card {id_} deleted')
    else:
        print(f'card {id_} not found')

def delete_card_ability():
    id_ = input("Enter the card ability's id: ")
    if card := Ability.find_by_id(id_):
        card.delete()
        print(f'card {id_} deleted')
    else:
        print(f'card {id_} not found')

def exit_program():
    print("Goodbye!")
    exit()