import unittest

from texas_holdem.main_game.poker import Poker, Card


class PokerTest(unittest.TestCase):
    def test_findRoyalFlush(self):
        poker = Poker()

        # best case scenario
        cards = [Card(1, 10), Card(1, 11), Card(
            1, 12), Card(1, 13), Card(1, 14)]
        hasRoyalFlush = poker.find_flush_royal(cards)
        self.assertTrue(hasRoyalFlush, "Cards should be a royal flush.")

        # test different suits, all high cards
        cards = [Card(2, 10), Card(1, 11), Card(
            1, 12), Card(1, 13), Card(1, 1)]
        hasRoyalFlush = poker.find_flush_royal(cards)
        self.assertFalse(
            hasRoyalFlush, "All cards should be of the same suit.")

        # test missing high card, same suits
        cards = [Card(1, 9), Card(1, 11), Card(1, 12), Card(1, 13), Card(1, 1)]
        hasRoyalFlush = poker.find_flush_royal(cards)
        self.assertFalse(
            hasRoyalFlush, "Should contain all high-cards[10,J,Q,K,A] cards.")

        # TODO: test repeated high card, same suits


if __name__ == '__main__':
    unittest.main()
