from models.__init__ import CONN, CURSOR
from models.card import Card
from models.card_type import Card_type

def seed_database():
    Card.drop_table()
    Card_type.drop_table()
    Card_type.create_table()
    Card.create_table()

# create seed data
    units = Card_type.create("Unit")
    spells = Card_type.create("Spell")
    landmarks = Card_type.create("Landmark")
    card1 = Card.create("Soldier", "Unit")
    card2 = Card.create("Wizard", "Unit")
    card3 = Card.create("Archer", "Unit")
    card4 = Card.create("Fireball", "Spell")
    card5 = Card.create("Lightning Bolt", "Spell")


seed_database()
print("Database seeded")