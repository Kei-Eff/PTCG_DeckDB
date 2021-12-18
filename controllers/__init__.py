
from controllers.user_settings_controller import user_settings
from controllers.card_controller import cards
from controllers.deck_controller import decks
from controllers.home_controller import home
from controllers.card_type_controller import card_types
from controllers.user_controller import users

registerable_controllers = [home, users, decks, card_types, cards, user_settings]
