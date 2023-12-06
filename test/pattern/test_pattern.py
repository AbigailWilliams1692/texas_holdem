###################################################
# @project: Texas Hold'em
# @file description: Test Pattern Classes
# @author: Abigail W
# @created on: 2023-12-02
# @last updated: 2023-12-06
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
import unittest

# Third-Party Packages

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

        # 测试是否符合同花顺牌型
        self.assertTrue(StraightFlush.isInstanceOf(hand1))
        self.assertFalse(StraightFlush.isInstanceOf(hand2))
        self.assertFalse(StraightFlush.isInstanceOf(hand3))
        self.assertTrue(StraightFlush.isInstanceOf(hand4))
        self.assertTrue(StraightFlush.isInstanceOf(hand5))

        # 测试手牌价值计算
        self.assertRaises(TypeError, StraightFlush.getHandValue, hand2)
        self.assertEqual(StraightFlush.getHandValue(hand1), [9, 9, 8, 7, 6, 5])
        self.assertEqual(StraightFlush.getHandValue(hand4), [9, 14, 13, 12, 11, 10])
        self.assertEqual(StraightFlush.getHandValue(hand5), [9, 5, 4, 3, 2, 1])

    def test_four_of_a_kind(self):
        # 测试四条牌型
        hand1 = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "5"), Card("♠", "A")])
        hand2 = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "A"), Card("♠", "A")])
        hand3 = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "A"), Card("♠", "Q")])
        hand4 = Hand([Card("♠", "7"), Card("♦", "7"), Card("♥", "7"), Card("♣", "7"), Card("♠", "A")])

        # 测试是否符合四条牌型
        self.assertTrue(FourOfAKind.isInstanceOf(hand1))
        self.assertFalse(FourOfAKind.isInstanceOf(hand2))
        self.assertFalse(FourOfAKind.isInstanceOf(hand3))
        self.assertTrue(FourOfAKind.isInstanceOf(hand4))

        # 测试手牌价值计算
        self.assertRaises(TypeError, FourOfAKind.getHandValue, hand2)
        self.assertRaises(TypeError, FourOfAKind.getHandValue, hand3)
        self.assertEqual(FourOfAKind.getHandValue(hand1), [8, 5, 14])
        self.assertEqual(FourOfAKind.getHandValue(hand4), [8, 7, 14])

    def test_full_house(self):
        # 测试葫芦牌型
        hand1 = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "A"), Card("♠", "A")])
        hand2 = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "A"), Card("♠", "K")])
        hand3 = Hand([Card("♠", "A"), Card("♦", "A"), Card("♥", "A"), Card("♣", "Q"), Card("♠", "Q")])
        hand4 = Hand([Card("♠", "2"), Card("♦", "2"), Card("♥", "2"), Card("♣", "A"), Card("♠", "A")])
        hand5 = Hand([Card("♠", "2"), Card("♦", "2"), Card("♥", "2"), Card("♣", "2"), Card("♠", "3")])

        # 测试是否符合葫芦牌型
        self.assertTrue(FullHouse.isInstanceOf(hand1))
        self.assertFalse(FullHouse.isInstanceOf(hand2))
        self.assertTrue(FullHouse.isInstanceOf(hand3))
        self.assertTrue(FullHouse.isInstanceOf(hand4))
        self.assertFalse(FullHouse.isInstanceOf(hand5))

        # 测试手牌价值计算
        self.assertRaises(TypeError, FullHouse.getHandValue, hand2)
        self.assertRaises(TypeError, FullHouse.getHandValue, hand5)
        self.assertEqual(FullHouse.getHandValue(hand1), [7, 5, 14])
        self.assertEqual(FullHouse.getHandValue(hand3), [7, 14, 12])
        self.assertEqual(FullHouse.getHandValue(hand4), [7, 2, 14])

    def test_flush(self):
        # 测试同花牌型
        hand1 = Hand([Card("♣", "5"), Card("♣", "10"), Card("♣", "J"), Card("♣", "2"), Card("♣", "K")])
        hand2 = Hand([Card("♠", "2"), Card("♠", "3"), Card("♠", "8"), Card("♠", "K"), Card("♠", "A")])
        hand3 = Hand([Card("♠", "2"), Card("♠", "3"), Card("♠", "8"), Card("♠", "K"), Card("♦", "A")])
        hand4 = Hand([Card("♠", "7"), Card("♦", "7"), Card("♥", "7"), Card("♣", "7"), Card("♠", "A")])

        # 测试是否符合同花牌型
        self.assertTrue(Flush.isInstanceOf(hand1))
        self.assertTrue(Flush.isInstanceOf(hand2))
        self.assertFalse(Flush.isInstanceOf(hand3))
        self.assertFalse(Flush.isInstanceOf(hand4))

        # 测试手牌价值计算
        self.assertRaises(TypeError, Flush.getHandValue, hand3)
        self.assertRaises(TypeError, Flush.getHandValue, hand4)
        self.assertEqual(Flush.getHandValue(hand1), [6, 13, 11, 10, 5, 2])
        self.assertEqual(Flush.getHandValue(hand2), [6, 14, 13, 8, 3, 2])

    def test_straight(self):
        # 测试顺子牌型
        hand1 = Hand([Card("♠", "5"), Card("♦", "2"), Card("♥", "4"), Card("♣", "3"), Card("♠", "A")])
        hand2 = Hand([Card("♠", "J"), Card("♦", "K"), Card("♥", "10"), Card("♣", "Q"), Card("♠", "A")])
        hand3 = Hand([Card("♠", "7"), Card("♦", "6"), Card("♥", "9"), Card("♣", "8"), Card("♠", "J")])
        hand4 = Hand([Card("♠", "2"), Card("♦", "2"), Card("♥", "3"), Card("♣", "4"), Card("♠", "5")])
        hand5 = Hand([Card("♠", "4"), Card("♠", "5"), Card("♠", "6"), Card("♠", "7"), Card("♠", "8")])

        # 测试是否符合顺子牌型
        self.assertTrue(Straight.isInstanceOf(hand1))
        self.assertTrue(Straight.isInstanceOf(hand2))
        self.assertFalse(Straight.isInstanceOf(hand3))
        self.assertFalse(Straight.isInstanceOf(hand4))
        self.assertTrue(Straight.isInstanceOf(hand5))

        # 测试手牌价值计算
        self.assertRaises(TypeError, Straight.getHandValue, hand3)
        self.assertRaises(TypeError, Straight.getHandValue, hand4)
        self.assertEqual(Straight.getHandValue(hand1), [5, 5, 4, 3, 2, 1])
        self.assertEqual(Straight.getHandValue(hand2), [5, 14, 13, 12, 11, 10])
        self.assertEqual(Straight.getHandValue(hand5), [5, 8, 7, 6, 5, 4])

    def test_three_of_a_kind(self):
        # 测试三条牌型
        hand1 = Hand([Card("♣", "K"), Card("♦", "K"), Card("♥", "K"), Card("♣", "2"), Card("♣", "4")])
        hand2 = Hand([Card("♠", "A"), Card("♦", "A"), Card("♣", "A"), Card("♠", "K"), Card("♠", "9")])
        hand3 = Hand([Card("♠", "A"), Card("♦", "A"), Card("♣", "A"), Card("♠", "K"), Card("♥", "K")])
        hand4 = Hand([Card("♠", "7"), Card("♦", "7"), Card("♥", "6"), Card("♣", "6"), Card("♠", "A")])

        # 测试是否符合三条牌型
        self.assertTrue(ThreeOfAKind.isInstanceOf(hand1))
        self.assertTrue(ThreeOfAKind.isInstanceOf(hand2))
        self.assertFalse(ThreeOfAKind.isInstanceOf(hand3))
        self.assertFalse(ThreeOfAKind.isInstanceOf(hand4))

        # 测试手牌价值计算
        self.assertRaises(TypeError, ThreeOfAKind.getHandValue, hand3)
        self.assertRaises(TypeError, ThreeOfAKind.getHandValue, hand4)
        self.assertEqual(ThreeOfAKind.getHandValue(hand1), [4, 13, 4, 2])
        self.assertEqual(ThreeOfAKind.getHandValue(hand2), [4, 14, 13, 9])

    def test_two_pairs(self):
        # 测试两对牌型
        hand1 = Hand([Card("♣", "K"), Card("♦", "K"), Card("♥", "10"), Card("♣", "10"), Card("♣", "4")])
        hand2 = Hand([Card("♠", "A"), Card("♦", "A"), Card("♣", "2"), Card("♠", "2"), Card("♠", "K")])
        hand3 = Hand([Card("♠", "A"), Card("♦", "A"), Card("♣", "A"), Card("♠", "K"), Card("♥", "K")])
        hand4 = Hand([Card("♠", "7"), Card("♦", "7"), Card("♥", "6"), Card("♣", "5"), Card("♠", "A")])

        # 测试是否符合两对牌型
        self.assertTrue(TwoPairs.isInstanceOf(hand1))
        self.assertTrue(TwoPairs.isInstanceOf(hand2))
        self.assertFalse(TwoPairs.isInstanceOf(hand3))
        self.assertFalse(TwoPairs.isInstanceOf(hand4))

        # 测试手牌价值计算
        self.assertRaises(TypeError, TwoPairs.getHandValue, hand3)
        self.assertRaises(TypeError, TwoPairs.getHandValue, hand4)
        self.assertEqual(TwoPairs.getHandValue(hand1), [3, 13, 10, 4])
        self.assertEqual(TwoPairs.getHandValue(hand2), [3, 14, 2, 13])

    def test_one_pair(self):
        # 测试一对牌型
        hand1 = Hand([Card("♣", "A"), Card("♦", "A"), Card("♥", "2"), Card("♣", "3"), Card("♣", "4")])
        hand2 = Hand([Card("♠", "A"), Card("♦", "10"), Card("♣", "2"), Card("♠", "2"), Card("♠", "K")])
        hand3 = Hand([Card("♠", "A"), Card("♦", "A"), Card("♣", "K"), Card("♠", "K"), Card("♥", "7")])
        hand4 = Hand([Card("♠", "7"), Card("♦", "7"), Card("♥", "6"), Card("♣", "6"), Card("♠", "6")])

        # 测试是否符合一对牌型
        self.assertTrue(OnePair.isInstanceOf(hand1))
        self.assertTrue(OnePair.isInstanceOf(hand2))
        self.assertFalse(OnePair.isInstanceOf(hand3))
        self.assertFalse(OnePair.isInstanceOf(hand4))

        # 测试手牌价值计算
        self.assertRaises(TypeError, OnePair.getHandValue, hand3)
        self.assertRaises(TypeError, OnePair.getHandValue, hand4)
        self.assertEqual(OnePair.getHandValue(hand1), [2, 14, 4, 3, 2])
        self.assertEqual(OnePair.getHandValue(hand2), [2, 2, 14, 13, 10])

    def test_high_card(self):
        # 测试高牌牌型
        hand1 = Hand([Card("♣", "A"), Card("♦", "8"), Card("♥", "7"), Card("♣", "2"), Card("♣", "Q")])
        hand2 = Hand([Card("♠", "K"), Card("♦", "3"), Card("♣", "9"), Card("♠", "10"), Card("♠", "J")])
        hand3 = Hand([Card("♠", "A"), Card("♦", "A"), Card("♣", "3"), Card("♠", "4"), Card("♥", "5")])
        hand4 = Hand([Card("♠", "7"), Card("♦", "8"), Card("♥", "9"), Card("♣", "10"), Card("♠", "J")])
        hand5 = Hand([Card("♠", "7"), Card("♠", "6"), Card("♠", "2"), Card("♠", "J"), Card("♠", "Q")])

        # 测试是否符合高牌牌型
        self.assertTrue(HighCard.isInstanceOf(hand1))
        self.assertTrue(HighCard.isInstanceOf(hand2))
        self.assertFalse(HighCard.isInstanceOf(hand3))
        self.assertFalse(HighCard.isInstanceOf(hand4))
        self.assertFalse(HighCard.isInstanceOf(hand5))

        # 测试手牌价值计算
        self.assertRaises(TypeError, HighCard.getHandValue, hand3)
        self.assertRaises(TypeError, HighCard.getHandValue, hand4)
        self.assertRaises(TypeError, HighCard.getHandValue, hand5)
        self.assertEqual(HighCard.getHandValue(hand1), [1, 14, 12, 8, 7, 2])
        self.assertEqual(HighCard.getHandValue(hand2), [1, 13, 11, 10, 9, 3])

    def test_inheritance(self):
        print(isinstance(StraightFlush, Pattern))


if __name__ == "__main__":
    unittest.main()