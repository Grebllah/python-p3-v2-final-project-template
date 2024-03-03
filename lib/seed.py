from models.__init__ import CONN, CURSOR
from models.card import Card
from models.card_type import Card_type

def seed_database():
    Card.drop_table()
    Card.create_table()

# create seed data
    card1 = Card.create("Soldier", "Unit")
    card2 = Card.create("Wizard", "Unit")
    card3 = Card.create("Archer", "Unit")
    card4 = Card.create("Fireball", "Spell")
    card5 = Card.create("Lightning Bolt", "Spell")

seed_database()
print("Database seeded")