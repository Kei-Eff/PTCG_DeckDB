# Pok&eacute;decks - Personal Pok&eacute;mon TCG Deck Manager

Pok&eacute;decks is a web application which users can use to manage their Pok&eacute;mon Trading Card Game decks. You can find more details about the purpose and design of this app in the [Design Document](/docs/T3A3_Design_Document).

## Current Features

* User signup/login
* Create/Update Deck
    - Users who have signed up and logged in are able to create a deck.
    - Deck names can also be updated.
* Create/Edit/Add Card (to Deck)
    - Users are able to create cards to include in a decklist.
    - Current fields accepted: Card 'Name', 'Set', 'Type', 'Quantity'
    - Future inclusion: Cost (per card)
    - Card details can be updated
* User Settings
    - Users are able to toggle between 'Dark Mode' and 'Anonymous Mode'
* Delete Deck/Card
    - Users are able to delete decks or cards they have created.
* View All Decks
    - (Login not required) Users are able to view a list of all decks submitted by all users on the site.
    - Decks are sorted by most recent added.
    - Anonymous users do not have they username displayed in the 'All Decks' page.


## How to Run

Clone repo

    ```
    git clone https://github.com/Kei-Eff/PTCG_DeckDB.git
    ```

Create, then activate

    ```
    virtualenv venv

    source venv/bin/activate
    ```
Install requirements

    ```
    pip install -r requirements.txt

    ```

