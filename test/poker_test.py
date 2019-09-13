from unittest import TestCase, main
from texas_holdem import Poker, Card


class PokerTest(TestCase):

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

        # test repeated high card, same suits
        cards = [Card(3, 10), Card(2, 10), Card(
            3, 12), Card(3, 13), Card(3, 1)]
        hasRoyalFlush = poker.find_royal_flush(cards)
        self.assertFalse(
            hasRoyalFlush, "Should not contain duplicate high-cards.")

    def test_find_straight_flush(self):
        poker = Poker()

        # best case scenario (out of order)
        cards = [Card(1, 5), Card(1, 8), Card(1, 7), Card(1, 6), Card(1, 9)]
        hasStraightFlush = poker.find_straight_flush(cards)
        self.assertTrue(hasStraightFlush, "Should be a straight flush.")

        # test missing card
        cards = [Card(1, 5), Card(1, 8), Card(1, 7), Card(1, 6), Card(1, 10)]
        hasStraightFlush = poker.find_straight_flush(cards)
        self.assertFalse(hasStraightFlush, "Should all be consecutive.")

        # test contains different suits
        cards = [Card(1, 5), Card(2, 8), Card(1, 7), Card(1, 6), Card(1, 9)]
        hasStraightFlush = poker.find_straight_flush(cards)
        self.assertFalse(hasStraightFlush, "Should be of the same suit.")

        # test contains duplicate
        cards = [Card(1, 5), Card(1, 5), Card(1, 7), Card(1, 6), Card(1, 8)]
        hasStraightFlush = poker.find_straight_flush(cards)
        self.assertFalse(hasStraightFlush, "Should have no duplicates.")

    def test_find_four_of_a_kind(self):
        poker = Poker()

        cards = [Card(1, 5), Card(2, 5), Card(2, 6), Card(3, 5), Card(4, 5)]
        hasFourOfAKind = poker.find_four_of_a_kind(cards)
        self.assertTrue(hasFourOfAKind, "Should have four of a kind.")


if __name__ == '__main__':
    main()
