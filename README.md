## Updating README.md

The card game creation and storage app:
This project is an Object Relational Mapping app using Python, which utilizes a Command Line Interface to allow a user to navigate, create, modify, or delete Instances of various classes representing Card Types, Cards, and Card abilities for any future potential card-based game. To run, open the lib/cli.py file using a python shell or terminal.

There are 3 classes the user can interact with:
1. Card Type - this class is where the user can create, update, or delete new Card types: essentially a way of categorizing the cards into various groups (historically in games like these this would be units/troops/creatures and spells/actions, but can be more involved, such as sub-types and type combinations, or more traditional, like the 4 suits)
2. Card Abilities - This is where the user can create, update, and delete abilities for the Cards. This is where the user can create Keywords or titles for the abilities, plus a short description of how the ability might work. This can range from something like a Unit having flying or double attack, or an Uno-like ability like "reverse" or "skip", or a value such as Ace, 2-9, Jack, Queen, King in a deck of cards.
3. Card - The Card class is the most important one, the one that utilizes the others. this is where the user can create, update, and delete individual cards, an object that has a Card Type and an Ability attached to it.

When the CLI program is initiated, the user will have several options. Inputting the number next to each option selects it. Some choices require further inputs. listed below are the choices and their explanations:
1. Exit the program - ends the loop, closing the CLI and returning to the terminal.
2. List all Cards - Prints a list of all current saved Card instances.
3. List all card Types - Prints a list of all current saved Card Type instances.
4. List all card Abilities - Prints a list of all current saved Card Ability instances.
5. Find card by name - Asks the user to input a name, and then seaches saved Cards for one with the inputted name, and returns that or an appropriate error.
6. Find card by ID number - Cards created are automatically given an unused ID number, user is asked to input a number, and then a search finds a saved Card with the input ID number, or an error if no such card exists.
7. List cards by card type - Prints a list of Cards that match Card Type with a user-inputted word.
8. List cards by card ability - Prints a list of Cards that match Card Ability with a user-inputted word.
9. Create a new card - Requests user input for card type and ability, then creates a new Card with the inputted choices as type and ability, provided they have already been created.
10. Create a new card type - requests user input for a name then creates a new Card Type object. Do this before creating new Cards of chosen type.
11. Create a new card ability - requests user input for a name and description, then creates a new Ability object. Do this before creating new cards with chosen Ability.
12. Delete a Card - requests a user input for Card Id number, then deletes the card associated with this number, or returns an error is no such object exists.
13. Delete card Type - requests a user input for Card Type Id number, then deletes the card type associated with this number, or returns an error is no such object exists.
14. Delete card Ability - requests a user input for Card Ability Id number, then deletes the ability associated with this number, or returns an error is no such object exists.
