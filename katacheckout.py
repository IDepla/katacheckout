from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Item:
    """ """

    name: str
    quantity: int
    price: float

    def __hash__(self) -> int:
        return hash(self.name)


class Basket:
    """ """

    items: Dict[Item, int]

    def __init__(self, items: Dict[Item, int] = None) -> None:
        if items is None:
            self.items = {}
        else:
            self.items = items

    def add(self, item: Item) -> None:
        if item in self.items:
            self.items[item] = self.items[item] + item.quantity
        else:
            self.items[item] = item.quantity

    def get_items(self):
        return self.items


class SpecialOffer(Item):
    """"""


class Order:
    """ """

    items: List[Item]
    offers_applied: List[SpecialOffer]
    total: float = 0
    partials: Dict[Item, float]


class CheckOut:
    """ """

    offers: List[SpecialOffer]

    def __init__(self) -> None:
        self.offers = []

    def register_offer(self, offer: SpecialOffer):
        """"""
        self.offers.append(offer)

    def lookup_offer(self, item: Item):
        for offer in self.offers:
            if offer.name == item.name:
                return offer

        return None

    def calculate(self, basket: Basket) -> Order:
        """calculate order"""
        order = Order()

        for item, quantity in basket.get_items().items():
            offer = self.lookup_offer(item)
            remaining_quantity = quantity
            if offer:
                # add applied offers
                offer_times = int(remaining_quantity / offer.quantity)
                order.total += offer_times * offer.price

                remaining_quantity = remaining_quantity % offer.quantity

            order.total += remaining_quantity * item.price

        return order
