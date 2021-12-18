# Pok&eacute;decks - Design Document

CCC-2021 T3A3 - Karl Alberto

---

## Purpose

The _Pok&eacute;decks_ app is designed as an online tool for managing a user/player's _Pokémon Trading Card Game_ cards and decks into _decklists_, using _SQLAlchemy_.

Individual decks will be stored in a table, which will hold a list of the individual cards the deck contains.

User information and account details will each be stored in separate tables, where a user is given the option to modify their site preferences (to achieve the one-to-one entity relationship requirement).

### Pages

List of pages in this app:
- Home Page (with Login/Signup)
- User Profile
- User Settings
- User Decks
- User Deck Cardlist
- All Decks (from all site users)
- Create New Deck
- Add Card

List of pages for future implementation (outside of assignment requirements)
- Card Search (linked to PTCG API)
- Card View


### Entity Relationship Diagram

![ERD for the PTCG DecklistDB website](T3A3_ERD.png)


## Data Validation and Integrity Errors

Lorem ipsum


## Security Concerns

Dolor


## Professional, Ethical and Legal Obligations

### Professional

This app is being developed as part of an assignment and portfolio item for the _Coding, Cloud and Cyber_ bootcamp.

### Ethical

The app currently does not apply a profanity filter; and as the series the game is based off of is very popular among younger children, there is risk of exposure to language that may be deemed inappropriate for their age.


### Legal

_Nintendo_ own the rights to the Pok&eacute;mon franchise, and are infamously litigious when it comes to use of their intellectual property. While many sites exist to support, rate, commentate on, and review the card game; concerns on whether Nintendo will apply legal pressure is never zero.

The current CSS framework used also has elements that are similarly designed to game elements from older Nintendo/Pok&eacute;mon games (namely from the older consoles), with some images based on the actual characters.