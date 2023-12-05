###################################################
# @project: Texas Hold'em
# @file description: Test Pattern Classes
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
from game.src.card.Hand import Hand
from game.src.pattern.Pattern import Pattern
from game.src.pattern.StraightFlush import StraightFlush
from game.src.pattern.FourOfAKind import FourOfAKind
from game.src.pattern.FullHouse import FullHouse
from game.src.pattern.Flush import Flush
from game.src.pattern.Straight import Straight
from game.src.pattern.ThreeOfAKind import ThreeOfAKind
from game.src.pattern.TwoPairs import TwoPairs
from game.src.pattern.OnePair import OnePair
from game.src.pattern.HighCard import HighCard


class TestingPatterns(unittest.TestCase):
    """
    测试牌型类
    """

    def test_straight_flush(self):
        # 测试同花顺牌型
        hand1 = Hand([Card("♠", "5"), Card("♠", "7"), Card("♠", "9"), Card("♠", "6"), Card("♠", "8")])
        hand2 = Hand([Card("♠", "5"), Card("♠", "J"), Card("♠", "9"), Card("♠", "10"), Card("♠", "8")])
        hand3 = Hand([Card("♠", "5"), Card("♦", "7"), Card("♠", "9"), Card("♠", "6"), Card("♠", "8")])
        hand4 = Hand([Card("♠", "A"), Card("♠", "K"), Card("♠", "Q"), Card("♠", "J"), Card("♠", "10")])
        hand5 = Hand([Card("♠", "A"), Card("♠", "2"), Card("♠", "3"), Card("♠", "4"), Card("♠", "5")])
        self.assertTrue(StraightFlush.isInstanceOf(hand1))
        self.assertFalse(StraightFlush.isInstanceOf(hand2))
        self.assertFalse(StraightFlush.isInstanceOf(hand3))

        self.assertRaises(TypeError, StraightFlush.getHandValue, hand2)
        self.assertEqual(StraightFlush.compareAtoB(hand4, hand1), 1)
        self.assertEqual(StraightFlush.compareAtoB(hand5, hand1), -1)

    def test_four_of_a_kind(self):
        hand1 = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "5"), Card("♠", "A")])
        hand2 = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "A"), Card("♠", "A")])
        hand3 = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "A"), Card("♠", "Q")])
        hand4 = Hand([Card("♠", "7"), Card("♦", "7"), Card("♥", "7"), Card("♣", "7"), Card("♠", "A")])
        pass

    def test_full_house(self):
        pass

    def test_flush(self):
        pass

    def test_straight(self):
        pass

    def test_three_of_a_kind(self):
        pass

    def test_two_pairs(self):
        pass

    def test_one_pair(self):
        pass

    def test_high_card(self):
        pass
