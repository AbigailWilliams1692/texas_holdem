###################################################
# @project: Texas Hold'em
# @file description: Test Card Class
# @author: Abigail W
# @created on: 2023-11-30
# @last updated: 2023-12-02
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
import unittest

# Customized Packages
from game.src.card.Card import Card


class TestingCard(unittest.TestCase):
    """
    测试扑克牌类
    """
    def test_set_up_card(self):
        # 测试生成一张牌
        card1 = Card(suit="♥", rank="A")
        self.assertEqual(str(card1), "♥A")

    def test_set_up_52_cards(self):
        # 测试生成52张牌
        for suit in Card.suits:
            for rank in Card.ranks:
                card = Card(suit=suit, rank=rank)
                self.assertEqual(repr(card), suit + rank)

    def test_validate_card(self):
        # 测试检查card1合法性
        card1 = Card("♣", "8")
        self.assertTrue(card1.validate(), f"{card1} should be valid.")
        # 测试card2 不合法
        card2 = Card("☆", "Z")
        self.assertFalse(card2.validate(), f"{card1} should be invalid.")

    def test_value_of_card(self):
        # 获取扑克牌的价值
        card1 = Card("♣", "10")
        self.assertEqual(card1.valueOfCard(), 10)
        card2 = Card("♦", "A")
        self.assertEqual(card2.valueOfCard(purpose="high"), 14)
        card3 = Card("♠", "A")
        self.assertEqual(card3.valueOfCard(purpose="low"), 1)
        card4 = Card("♥", "A")
        self.assertRaises(ValueError, card4.valueOfCard, None)

    def test_compare_value(self):
        card1 = Card("♣", "3")
        card2 = Card("♦", "A")
        card3 = Card("♠", "J")
        card4 = Card("♥", "J")
        self.assertEqual(card1.compareTo(card2), -1)
        self.assertEqual(card3.compareTo(card1), 1)
        self.assertEqual(card2.compareTo(card4), 1)
        self.assertEqual(card3.compareTo(card4), 0)

    def test_compare_Value(self):
        card1 = Card("♣", "3")
        card2 = Card("♦", "A")
        card3 = Card("♠", "J")
        card4 = Card("♥", "J")
        self.assertEqual(Card.compareValue(card1, card2), -1)
        self.assertEqual(Card.compareValue(card3, card1), 1)
        self.assertEqual(Card.compareValue(card2, card4), 1)
        self.assertEqual(Card.compareValue(card3, card4), 0)

    def test_is_same_suit(self):
        card1 = Card("♣", "3")
        card2 = Card("♦", "A")
        card3 = Card("♦", "J")
        self.assertFalse(card1.isSameSuit(card2))
        self.assertTrue(card2.isSameSuit(card3))

    def test_compare_Suit(self):
        card1 = Card("♣", "3")
        card2 = Card("♦", "A")
        card3 = Card("♦", "J")
        self.assertFalse(Card.compareSuit(card1, card2))
        self.assertTrue(Card.compareSuit(card2, card3))

    def test_convert_rank_to_value(self):
        card1 = Card("♣", "3")
        card2 = Card("♦", "A")
        card3 = Card("♦", "J")
        self.assertEqual(Card.convertRankToValue(card1.get_rank), 3)
        self.assertEqual(Card.convertRankToValue(card2.get_rank), 14)
        self.assertEqual(Card.convertRankToValue(card2.get_rank, purpose="low"), 1)
        self.assertEqual(Card.convertRankToValue(card3.get_rank), 11)

    def test_equal_card(self):
        card1 = Card("♣", "4")
        card2 = Card("♦", "J")
        card3 = Card("♦", "J")
        self.assertFalse(card1 == card2)
        self.assertTrue(card2 == card3)


if __name__ == "__main__":
    unittest.main()
