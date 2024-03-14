from models.__init__ import CONN, CURSOR
from models.card import Card
from models.card_type import Card_type
from models.ability import Ability

def seed_database():
    Card.drop_table()
    Card_type.drop_table()
    Ability.drop_table()
    Card_type.create_table()
    Card.create_table()
    Ability.create_table()
    units = Card_type.create("Unit")
    spells = Card_type.create("Spell")
    landmarks = Card_type.create("Landmark")
    ability1 = Ability.create("Strong", "Unit does more damage in combat.")
    card1 = Card.create("Soldier", "Unit", "Strong")
    card2 = Card.create("Wizard", "Unit", "")
    card3 = Card.create("Archer", "Unit", "")
    card4 = Card.create("Fireball", "Spell", "")
    card5 = Card.create("Lightning Bolt", "Spell", "")

seed_database()
print("Database seeded")