from models.card_type import Card_type
from models.card import Card
from models.ability import Ability

def clear_database():
    Card.drop_table()
    Card_type.drop_table()
    Ability.drop_table()
    Card_type.create_table()
    Card.create_table()
    Ability.create_table()

clear_database()