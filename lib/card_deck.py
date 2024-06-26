from models.card_type import Card_type
from models.card import Card
from models.ability import Ability

def create_deck():
    Card.drop_table()
    Card_type.drop_table()
    Ability.drop_table()
    Card_type.create_table()
    Card.create_table()
    Ability.create_table()

    spades = Card_type.create("Spade")
    hearts = Card_type.create("Heart")
    clubs = Card_type.create("Club")
    diamonds = Card_type.create("Diamond")

    ace = Ability.create("Ace", "Worth 11")
    two = Ability.create("2", "Worth 2")
    three = Ability.create("3", "Worth 3")
    four = Ability.create("4", "Worth 4")
    five = Ability.create("5", "Worth 5")
    six = Ability.create("6", "Worth 6")
    seven = Ability.create("7", "Worth 7")
    eight = Ability.create("8", "Worth 8")
    nine = Ability.create("9", "Worth 9")
    ten = Ability.create("10", "Worth 10")
    jack = Ability.create("Jack", "Worth 10")
    queen = Ability.create("Queen", "Worth 10")
    king = Ability.create("King", "Worth 10")

    Ace_of_spades = Card.create("Ace of Spades", "Spade", "Ace")
    Ace_of_clubs = Card.create("Ace of Clubs", "Club", "Ace")
    Ace_of_hearts = Card.create("Ace of Hearts", "Heart", "Ace")
    Ace_of_diamonds = Card.create("Ace of Diamonds", "Diamond", "Ace")
    two_of_spades = Card.create("2 of Spades", "Spade", "2")
    two_of_clubs = Card.create("2 of Clubs", "Club", "2")
    two_of_hearts = Card.create("2 of Hearts", "Heart", "2")
    two_of_diamonds = Card.create("2 of Diamonds", "Diamond", "2")
    three_of_spades = Card.create("3 of Spades", "Spade", "3")
    three_of_clubs = Card.create("3 of Clubs", "Club", "3")
    three_of_hearts = Card.create("3 of Hearts", "Heart", "3")
    three_of_diamonds = Card.create("3 of Diamonds", "Diamond", "3")
    four_of_spades = Card.create("4 of Spades", "Spade", "4")
    four_of_clubs = Card.create("4 of Clubs", "Club", "4")
    four_of_hearts = Card.create("4 of Hearts", "Heart", "4")
    four_of_diamonds = Card.create("4 of Diamonds", "Diamond", "4")
    five_of_spades = Card.create("5 of Spades", "Spade", "5")
    five_of_clubs = Card.create("5 of Clubs", "Club", "5")
    five_of_hearts = Card.create("5 of Hearts", "Heart", "5")
    five_of_diamonds = Card.create("5 of Diamonds", "Diamond", "5")
    six_of_spades = Card.create("6 of Spades", "Spade", "6")
    six_of_clubs = Card.create("6 of Clubs", "Club", "6")
    six_of_hearts = Card.create("6 of Hearts", "Heart", "6")
    six_of_diamonds = Card.create("6 of Diamonds", "Diamond", "6")
    seven_of_spades = Card.create("7 of Spades", "Spade", "7")
    seven_of_clubs = Card.create("7 of Clubs", "Club", "7")
    seven_of_hearts = Card.create("7 of Hearts", "Heart", "7")
    seven_of_diamonds = Card.create("7 of Diamonds", "Diamond", "7")
    eight_of_spades = Card.create("8 of Spades", "Spade", "8")
    eight_of_clubs = Card.create("8 of Clubs", "Club", "8")
    eight_of_hearts = Card.create("8 of Hearts", "Heart", "8")
    eight_of_diamonds = Card.create("8 of Diamonds", "Diamond", "8")
    nine_of_spades = Card.create("9 of Spades", "Spade", "9")
    nine_of_clubs = Card.create("9 of Clubs", "Club", "9")
    nine_of_hearts = Card.create("9 of Hearts", "Heart", "9")
    nine_of_diamonds = Card.create("9 of Diamonds", "Diamond", "9")
    ten_of_spades = Card.create("10 of Spades", "Spade", "10")
    ten_of_clubs = Card.create("10 of Clubs", "Club", "10")
    ten_of_hearts = Card.create("10 of Hearts", "Heart", "10")
    ten_of_diamonds = Card.create("10 of Diamonds", "Diamond", "10")
    jack_of_spades = Card.create("Jack of Spades", "Spade", "Jack")
    jack_of_clubs = Card.create("Jack of Clubs", "Club", "Jack")
    jack_of_hearts = Card.create("Jack of Hearts", "Heart", "Jack")
    jack_of_diamonds = Card.create("Jack of Diamonds", "Diamond", "Jack")
    queen_of_spades = Card.create("Queen of Spades", "Spade", "Queen")
    queen_of_clubs = Card.create("Queen of Clubs", "Club", "Queen")
    queen_of_hearts = Card.create("Queen of Hearts", "Heart", "Queen")
    queen_of_diamonds = Card.create("Queen of Diamonds", "Diamond", "Queen")
    king_of_spades = Card.create("King of Spades", "Spade", "King")
    king_of_clubs = Card.create("King of Clubs", "Club", "King")
    king_of_hearts = Card.create("King of Hearts", "Heart", "King")
    king_of_diamonds = Card.create("King of Diamonds", "Diamond", "King")

create_deck()
    
