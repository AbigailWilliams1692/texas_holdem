###################################################
# @project: Texas Hold'em
# @file description: Test Evaluator Classes
# @author: Abigail W
# @created on: 2023-12-06
# @last updated: 2023-12-06
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
import time
import unittest

# Third-Party Packages

# Customized Packages
from game.src.card.Card import Card
from game.src.card.TexasDeck import TexasDeck
from game.src.card.Hand import Hand
# from game.src.pattern.Pattern import Pattern
from game.src.pattern.StraightFlush import StraightFlush
from game.src.pattern.FourOfAKind import FourOfAKind
from game.src.pattern.FullHouse import FullHouse
from game.src.pattern.Flush import Flush
from game.src.pattern.Straight import Straight
from game.src.pattern.ThreeOfAKind import ThreeOfAKind
from game.src.pattern.TwoPairs import TwoPairs
from game.src.pattern.OnePair import OnePair
from game.src.pattern.HighCard import HighCard
from game.src.evaluator.HandEvaluator import HandEvaluator


class TestingEvaluator(unittest.TestCase):
    """
    测试Evaluator
    """

    def test_hand_evaluator_pattern_calculation(self):
        # set up
        hand_evaluator = HandEvaluator()
        hand1 = Hand([Card("♠", "5"), Card("♠", "7"), Card("♠", "9"), Card("♠", "6"), Card("♠", "8")])
        hand2 = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "5"), Card("♠", "A")])
        hand3 = Hand([Card("♠", "A"), Card("♦", "A"), Card("♥", "A"), Card("♣", "Q"), Card("♠", "Q")])
        hand4 = Hand([Card("♠", "J"), Card("♦", "K"), Card("♥", "10"), Card("♣", "Q"), Card("♠", "A")])
        hand5 = Hand([Card("♠", "5"), Card("♦", "2"), Card("♥", "4"), Card("♣", "3"), Card("♠", "A")])
        hand6 = Hand([Card("♠", "2"), Card("♠", "3"), Card("♠", "8"), Card("♠", "K"), Card("♠", "A")])
        hand7 = Hand([Card("♠", "J"), Card("♦", "J"), Card("♥", "J"), Card("♣", "10"), Card("♠", "3")])
        hand8 = Hand([Card("♠", "J"), Card("♦", "J"), Card("♥", "10"), Card("♣", "10"), Card("♠", "3")])
        hand9 = Hand([Card("♠", "J"), Card("♦", "J"), Card("♥", "10"), Card("♣", "9"), Card("♠", "3")])
        hand10 = Hand([Card("♠", "J"), Card("♦", "4"), Card("♥", "10"), Card("♣", "9"), Card("♠", "3")])

        # 测试牌型计算
        self.assertEqual(hand_evaluator.calculateHandPattern(hand1), StraightFlush)
        self.assertEqual(hand_evaluator.calculateHandPattern(hand2), FourOfAKind)
        self.assertEqual(hand_evaluator.calculateHandPattern(hand3), FullHouse)
        self.assertEqual(hand_evaluator.calculateHandPattern(hand4), Straight)
        self.assertEqual(hand_evaluator.calculateHandPattern(hand5), Straight)
        self.assertEqual(hand_evaluator.calculateHandPattern(hand6), Flush)
        self.assertEqual(hand_evaluator.calculateHandPattern(hand7), ThreeOfAKind)
        self.assertEqual(hand_evaluator.calculateHandPattern(hand8), TwoPairs)
        self.assertEqual(hand_evaluator.calculateHandPattern(hand9), OnePair)
        self.assertEqual(hand_evaluator.calculateHandPattern(hand10), HighCard)

    def test_hand_evaluator_comparison(self):
        # set up
        hand_evaluator = HandEvaluator()

        hand1A = Hand([Card("♠", "5"), Card("♦", "5"), Card("♥", "5"), Card("♣", "5"), Card("♠", "A")])
        hand1B = Hand([Card("♠", "7"), Card("♦", "7"), Card("♥", "7"), Card("♣", "7"), Card("♠", "10")])
        hand1C = Hand([Card("♠", "7"), Card("♦", "7"), Card("♥", "7"), Card("♣", "7"), Card("♠", "J")])

        hand2A = Hand([Card("♠", "A"), Card("♦", "A"), Card("♥", "A"), Card("♣", "Q"), Card("♠", "Q")])
        hand2B = Hand([Card("♠", "A"), Card("♦", "A"), Card("♥", "A"), Card("♣", "K"), Card("♠", "K")])
        hand2C = Hand([Card("♠", "10"), Card("♦", "10"), Card("♥", "10"), Card("♣", "Q"), Card("♠", "Q")])

        hand3A = Hand([Card("♠", "J"), Card("♦", "K"), Card("♥", "10"), Card("♣", "Q"), Card("♠", "A")])
        hand3B = Hand([Card("♠", "5"), Card("♦", "2"), Card("♥", "4"), Card("♣", "3"), Card("♠", "A")])

        hand4A = Hand([Card("♠", "2"), Card("♠", "3"), Card("♠", "8"), Card("♠", "Q"), Card("♠", "A")])
        hand4B = Hand([Card("♠", "2"), Card("♠", "3"), Card("♠", "8"), Card("♠", "K"), Card("♠", "A")])

        # 测试牌型计算
        self.assertEqual(hand_evaluator.compareAtoB(A=hand1A, B=hand1B), -1)
        self.assertEqual(hand_evaluator.compareAtoB(A=hand1B, B=hand1C), -1)
        self.assertEqual(hand_evaluator.compareAtoB(A=hand1C, B=hand1A), 1)

        self.assertEqual(hand_evaluator.compareAtoB(A=hand2A, B=hand2B), -1)
        self.assertEqual(hand_evaluator.compareAtoB(A=hand2B, B=hand2C), 1)
        self.assertEqual(hand_evaluator.compareAtoB(A=hand2C, B=hand2A), -1)

        self.assertEqual(hand_evaluator.compareAtoB(A=hand3A, B=hand3B), 1)

        self.assertEqual(hand_evaluator.compareAtoB(A=hand4A, B=hand4B), -1)

    def test_hand_evaluator_random(self):
        # set up
        deck = TexasDeck()
        hand_evaluator = HandEvaluator()

        # 循环测试
        for i in range(100):
            # 抽卡
            hand1 = Hand(deck.drawNCards(n=5))
            hand2 = Hand(deck.drawNCards(n=5))

            # 计算
            hand1_pattern, hand2_pattern = hand_evaluator.calculateHandPattern(hand1), hand_evaluator.calculateHandPattern(hand2)
            comparison_result = hand_evaluator.compareAtoB(A=hand1, B=hand2)
            comparison_result_symbol = ">" if comparison_result == 1 else ("<" if comparison_result == -1 else "=")

            # 输出结果
            print(f"{hand1} is of {hand1_pattern.getPatternName()} pattern.")
            print(f"{hand2} is of {hand2_pattern.getPatternName()} pattern.")
            print(f"{hand1}  {comparison_result_symbol}  {hand2}")
            print()

            # 重置牌堆
            deck.reset()

    def test_hand_evaluator_random_rare(self):
        # set up
        deck = TexasDeck()
        hand_evaluator = HandEvaluator()
        N = 10000
        threshold = 7

        # 循环测试
        t1 = time.time()
        counter = 0

        for i in range(N):
            # 抽卡
            hand1 = Hand(deck.drawNCards(n=5))
            hand2 = Hand(deck.drawNCards(n=5))

            # 计算
            hand1_pattern, hand2_pattern = hand_evaluator.calculateHandPattern(hand1), hand_evaluator.calculateHandPattern(hand2)
            comparison_result = hand_evaluator.compareAtoB(A=hand1, B=hand2)
            comparison_result_symbol = ">" if comparison_result == 1 else ("<" if comparison_result == -1 else "=")

            # 输出结果
            if hand1_pattern.getPatternValue() >= threshold or hand2_pattern.getPatternValue() >= threshold:
                counter += 1
                print(f"{hand1} is of {hand1_pattern.getPatternName()} pattern.")
                print(f"{hand2} is of {hand2_pattern.getPatternName()} pattern.")
                print(f"{hand1}  {comparison_result_symbol}  {hand2}")
                print()

            # 重置牌堆
            deck.reset()

        # 计时结束
        t2 = time.time()
        print(f"循环{N}次，共输出{counter}次，用时{t2-t1: .2f}秒。")


if __name__ == "__main__":
    unittest.main()
