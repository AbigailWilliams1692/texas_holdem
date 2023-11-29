###################################################
# @project: Texas Hold'em
# @file description: Card class
# @author: Abigail W
# @created on: 2023-11-30
# @last updated: 2023-11-30
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
import unittest

# Customized Packages
from resources.src.card.Card import Card


class TestingCard(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
