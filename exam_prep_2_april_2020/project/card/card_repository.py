from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards: list = []
        self.cards_names: set = set()

    @property
    def count(self):
        return len(self.cards)

    def add(self, card: Card):
        if card.name in self.cards_names:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.cards_names.add(card.name)

    def remove(self, card: str):
        if not card:
            raise ValueError("Card cannot be an empty string!")
        card_obj = self.find(card)
        if card_obj:
            self.cards.remove(card_obj)
            self.cards_names.remove(card_obj.name)

    def find(self, name: str):
        obj = [c for c in self.cards if c.name == name][0]
        if obj:
            return obj
