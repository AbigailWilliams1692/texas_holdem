###################################################
# @project: Texas Hold'em
# @file description: Test Texas Deck Class
# @author: Abigail W
# @created on: 2023-12-02
# @last updated: 2023-12-02
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
import unittest

# Third-Party Packages
import numpy as np

# Customized Packages
from game.src.card.Card import Card
from game.src.card.TexasDeck import TexasDeck


class TestingTexasDeck(unittest.TestCase):
    """
    测试牌堆类
    """
    def test_set_up(self):
        # 测试生成一副扑克牌
        deck = TexasDeck()
        # 测试扑克牌数量
        self.assertEqual(deck.getLength(), 52)
        # 测试每一张扑克牌都符合要求
        for card in deck.get_deck:
            self.assertIsInstance(card, Card)
            self.assertTrue(card.validate())

    def test_get_random_number_generator(self):
        # 测试生成一副扑克牌
        deck = TexasDeck()
        # 测试扑克牌数量
        self.assertEqual(deck.get_random_generator, np.random)

    def test_set_deck(self):
        # 测试设定扑克牌的牌堆
        deck1 = TexasDeck()
        deck1.set_deck(new_deck=[Card("♣", "7"), Card("♥", "K")])
        deck2 = TexasDeck(list_of_cards=[Card("♣", "7"), Card("♥", "K")])
        self.assertEqual(deck1, deck2)

    def test_validate_each_card(self):
        # 测试牌堆中每一张牌是否合法
        deck1 = TexasDeck()
        deck2 = TexasDeck(list_of_cards=[Card("♣", "9"), Card("♣", "10")])
        deck3 = TexasDeck(list_of_cards=[Card("♣", "9"), Card("♣", "10"), Card("☆", "K")])
        self.assertTrue(deck1.validateEachCard(), "1")
        self.assertTrue(deck2.validateEachCard(), "2")
        self.assertFalse(deck3.validateEachCard(), "3")

    def test_validate_whole(self):
        # 测定整副牌是否满足出厂合法性
        deck1 = TexasDeck()
        deck2 = deck1.copy()
        deck2.drawCard()
        deck3 = TexasDeck(list_of_cards=[Card(suit, rank) for suit in ("□", "○", "△", "☆") for rank in Card.ranks])
        deck4 = TexasDeck(list_of_cards=[Card("♣", "9") for _ in range(52)])
        self.assertTrue(deck1.validateWhole(), "1")
        self.assertFalse(deck2.validateWhole(), "2")
        self.assertFalse(deck3.validateWhole(), "3")
        self.assertFalse(deck4.validateWhole(), "4")

    def test_copy_and_shuffle(self):
        # 测试洗牌
        deck1 = TexasDeck()
        deck2 = deck1.copy()
        deck1.shuffle()
        self.assertNotEqual(deck1, deck2)

    def test_draw_card(self):
        # 测试抽牌
        deck = TexasDeck(list_of_cards=[Card("♣", "9"), Card("♣", "10")])
        card1 = deck.drawCard()
        card2 = deck.drawCard()
        card3 = deck.drawCard()
        self.assertEqual(card1, Card("♣", "10"))
        self.assertEqual(card2, Card("♣", "9"))
        self.assertIsNone(card3)

    def test_draw_N_cards(self):
        # 测试抽取N张牌
        deck = TexasDeck()
        card_list1 = deck.drawNCards(2)
        card_list2 = deck.drawNCards(20)
        self.assertRaises(ValueError, deck.drawNCards, 100)
        card_list3 = deck.drawNCards(30)
        self.assertEqual(len(card_list1), 2)
        self.assertEqual(len(card_list2), 20)
        self.assertEqual(len(card_list3), 30)


if __name__ == "__main__":
    unittest.main()
