import unittest

from texas_holdem.main_game.poker import Poker, Card


class PokerTest(unittest.TestCase):
    def test_find_royal_flush(self):
        poker = Poker()

        # best case scenario
        cards = [Card(1, 10), Card(1, 11), Card(
            1, 12), Card(1, 13), Card(1, 1)]
        hasRoyalFlush = poker.find_royal_flush(cards)
        self.assertTrue(hasRoyalFlush, "Should be a royal flush.")

        # test different suits, all high cards
        cards = [Card(2, 10), Card(1, 11), Card(
            1, 12), Card(1, 13), Card(1, 1)]
        hasRoyalFlush = poker.find_royal_flush(cards)
        self.assertFalse(
            hasRoyalFlush, "All cards should be of the same suit.")

        # test missing high card, same suits
        cards = [Card(1, 9), Card(1, 11), Card(1, 12), Card(1, 13), Card(1, 1)]
        hasRoyalFlush = poker.find_royal_flush(cards)
        self.assertFalse(
            hasRoyalFlush, "Should contain all high-cards.")

        # TODO: test repeated high card, same suits
        cards = [Card(3, 10), Card(2, 10), Card(
            3, 12), Card(3, 13), Card(3, 1)]
        hasRoyalFlush = poker.find_royal_flush(cards)
        self.assertFalse(
            hasRoyalFlush, "Should not contain duplicate high-cards.")


if __name__ == '__main__':
    unittest.main()
