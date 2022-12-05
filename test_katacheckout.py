import unittest

from katacheckout import Item, Basket, Order, CheckOut, SpecialOffer


class CheckoutTestCase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_one_a_cost_30(self):
        basket = Basket()
        basket.add(Item("A", 1, 30.0))

        checkout = CheckOut()

        result = checkout.calculate(basket)

        self.assertEqual(result.total, 30)

    def test_add_item_in_basket(self):
        basket = Basket()
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("A", 1, 50.0))

        checkout = CheckOut()

        result = checkout.calculate(basket)

        self.assertEqual(result.total, 100)

    def test_two_items_in_basket(self):
        basket = Basket()
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("B", 1, 30.0))

        checkout = CheckOut()

        result = checkout.calculate(basket)

        self.assertEqual(result.total, 80)

    def test_three_items_in_basket(self):
        basket = Basket()
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("B", 1, 30.0))
        basket.add(Item("C", 1, 10.0))

        checkout = CheckOut()

        result = checkout.calculate(basket)

        self.assertEqual(result.total, 90)

    def test_multi_item_in_the_basket(self):
        basket = Basket()
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("B", 1, 30.0))
        basket.add(Item("C", 1, 10.0))

        checkout = CheckOut()

        result = checkout.calculate(basket)

        self.assertEqual(result.total, 190)
        # self.assertEqual(result["A"].total, 150)
        # self.assertEqual(result["B"].total, 30)
        # self.assertEqual(result["C"].total, 10)

    def test_special_offer(self):
        basket = Basket()
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("B", 1, 30.0))
        basket.add(Item("C", 1, 10.0))

        checkout = CheckOut()

        checkout.register_offer(SpecialOffer("A", 2, 80))

        result = checkout.calculate(basket)

        self.assertEqual(result.total, 170)
        # self.assertEqual(result["A"].total, 130)
        # self.assertEqual(result["B"].total, 30)
        # self.assertEqual(result["C"].total, 10)

    def test_multiple_special_offer(self):
        basket = Basket()
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("A", 1, 50.0))
        basket.add(Item("B", 1, 30.0))
        basket.add(Item("B", 1, 30.0))

        checkout = CheckOut()

        checkout.register_offer(SpecialOffer("A", 2, 30))
        checkout.register_offer(SpecialOffer("B", 2, 30))

        result = checkout.calculate(basket)

        self.assertEqual(result.total, 110)
        # self.assertEqual(result["A"].total, 80)
        # self.assertEqual(result["B"].total, 30)
