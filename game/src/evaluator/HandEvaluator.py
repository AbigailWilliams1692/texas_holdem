###################################################
# @project: Texas Hold'em
# @file description: Hand Evaluator, which evaluates and compares each Hand
# @author: Abigail W
# @created on: 2023-12-06
# @last updated: 2023-12-06
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
from abc import ABC, abstractmethod

# Third-Party Packages
import numpy as np

# Customized Packages
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


class HandEvaluator(ABC):
    """
    手牌估值比较器
    """

    #######################################################################
    # Class attributes
    #######################################################################
    ranked_patterns: list[Pattern] = [HighCard, OnePair, TwoPairs, ThreeOfAKind, Straight, Flush, FullHouse,
                                      FourOfAKind, StraightFlush]

    #######################################################################
    # Initialization
    #######################################################################
    def __init__(self):
        pass

    #######################################################################
    # Getter & Setter methods
    #######################################################################

    #######################################################################
    # Instance methods
    #######################################################################
    def calculateHandPattern(self, hand: Hand):
        """
        该方法计算一手牌的牌型，按照ranked_patterns的顺序从低到高进行测试；
        除顺子和同花要进行额外一步测试是否符合同花顺以外，其他牌型有短路逻辑。

        :param hand: 手牌，Hand类。
        :return: 牌型。
        """
        for pattern in self.ranked_patterns:
            if pattern.isInstanceOf(hand):
                if pattern in [Straight, Flush] and StraightFlush.isInstanceOf(hand):
                    return StraightFlush
                else:
                    return pattern
        return

    def compareAtoB(self, A: Hand, B: Hand) -> int:
        """
        该方法比较手牌A和手牌B并返回-1, 0, 1以表示哪个手牌更大。
        -1 代表 A<B, 0 代表 A=B, 1 代表 A>B。

        :param A: 手牌A，Hand类。
        :param B: 手牌A，Hand类。
        :return: -1, 0, 1
        """
        # 先判断手牌的牌型
        pattern_A, pattern_B = self.calculateHandPattern(A), self.calculateHandPattern(B)

        # 获取手牌的对应价值
        values_A, values_B = pattern_A.getHandValue(A), pattern_B.getHandValue(B)

        # 进行比较 （通用比较方式）
        min_length = min(len(values_A), len(values_B))
        for i in range(min_length):
            if values_A[i] > values_B[i]:
                # 手牌A > 手牌B
                return 1
            elif values_A[i] < values_B[i]:
                # 手牌A < 手牌B
                return -1

        # 如果循环完成还没有分出高低，就返回0，手牌A = 手牌B
        return 0

    #######################################################################
    # Utils
    #######################################################################
