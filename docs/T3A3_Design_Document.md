# Pok&eacute;decks - Design Document

CCC-2021 T3A3 - Karl Alberto

---

## Purpose

The _Pok&eacute;decks_ app is designed as an online tool for managing a user/player's _Pokémon Trading Card Game (PTCG)_ cards into _decks_ and _decklists*_. This app is being developed as part of an assignment and portfolio item for the **Coder Academy** ___Coding, Cloud and Cyber___ Bootcamp.

Individual decks are stored in a table, while individual cards are stored in another. For now, each individual card needs to be created by the user. Unfortunately, as each card in a cardlist is added one by one, there is currently no way to avoid duplicate instances of the same card (in separate decks).

Future development work will include the use of the [PTCG API](https://dev.pokemontcg.io/), so that users have proper 'Card Search' functionality, and to also avoid the duplicate entities issue mentioned. More details are available below in 'Professional Obligations' section.

Basic user information and account details will be stored in separate tables, where a user is given the option to modify their site settings (to achieve the one-to-one entity relationship requirement). Current user details required are username, email address, and password. Current site settings available for each user are 'Dark Mode' and 'Anonymous Mode'. Dark Mode is provided as a readability/accesibility option; while Anonymous Mode makes the owner of the deck anonymous to other users of the website.

_(*"Decklist" is the conventional TCG term for the list of cards in a deck. For the purposes of this site/app, the decklist is referred to as a "Cardlist", where decklist may sound like a term used for a list of decks, rather than a list of cards in a deck)_

### Pages

#### List of pages in this app:
* Home Page (with Login/Signup)
    - Short welcome message, with navbar to other pages available on the site.
* User Profile & Settings
    - Shows the current logged in user their details, along with tickbox options to enable either 'Dark Mode' and/or 'Anonymous Mode'.
* My Decks
    - Shows a table of the decks the current user has created.
* User (Deck) Cardlist
    - Displays the list of cards contained within a deck.
* All Decks (from all users of this site)
    - Displays a list of all decks created by all users on the site, _ordered by_ last created.
* Create New Deck / Update Deck
    - Allows a logged in user to name and create a new deck. Update allows the deck name to be updated by the deck's owner.
* Add Card / Update
    - A form page where a user can add a card to a deck by filling in the required fields. All fields need to be populated for a card to be submitted. Update allows details of a card in a deck to be modified.

#### List of pages for future implementation (outside of assignment requirements):
* Card Search (linked to PTCG API)
    - Planned to allow users to search for specific cards that exist within the game. API access will also limit the need to store individual cards in our own database, as we can query the required cards from the API.
* Card View
    - Will show an image of the actual card selected.
* Contact Page
    - To allow users to raise concerns, and submit questions about the site.


### Entity Relationship Diagram

![ERD for the PTCG DecklistDB website](T3A3_ERD.png)


## Data Validation and Integrity Errors

Lorem ipsum


## Security Concerns

Current concerns include:

* No password confirmation step
* No password or email address update capability
* 


## Professional, Ethical and Legal Obligations

### Professional





### Ethical

The app currently does not apply a profanity filter; and as the series the game is based off of is very popular among younger children, there is risk of exposure to language that may be deemed inappropriate for their age.


### Legal

_Nintendo_ own the rights to the Pok&eacute;mon franchise, and are infamously litigious when it comes to use of their intellectual property. While many sites exist to support, rate, commentate on, and review the card game; concerns on whether Nintendo will apply legal pressure is never zero.

The current CSS framework used also has elements that are similarly designed to game elements from older Nintendo/Pok&eacute;mon games (namely from the older consoles), with some images based on the actual characters.