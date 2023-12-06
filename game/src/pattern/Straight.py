###################################################
# @project: Texas Hold'em
# @file description: Straight class
# @author: Abigail W
# @created on: 2023-11-23
# @last updated: 2023-11-30
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
from abc import ABC
from collections import Counter

# Third-Party Packages
import numpy as np

# Customized Packages
from game.src.card.Card import Card
from game.src.card.Hand import Hand
from game.src.pattern.Pattern import Pattern


class Straight(Pattern, ABC):
    """
    顺子牌型
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = "Straight"
    value = 5
    rank_counts_benchmark = [1, 1, 1, 1, 1]

    @staticmethod
    def isContinuous(arr: list[int]) -> bool:
        """
        辅助函数，以测试一列升序整数是否连续（间隔为1）。

        :param arr: a list of increasing integers with interval 1.
        :return: True or False
        """
        return all([(arr[i] - 1) == arr[i + 1] for i in range(len(arr) - 1)])

    @classmethod
    def isInstanceOf(cls, hand: Hand) -> bool:
        """
        判断list_of_cards是否为顺子牌型，是则返回True，否则返回False。

        :param hand: Hand类对象，判定的对象
        :return: True/False
        """
        # 获取手牌的所有ranks
        ranks = hand.getRanks()

        # 用Counter类型对手牌进行计数
        rank_counts = Counter(ranks)

        # 首先排除任何Counter.values()不是[1, 1, 1, 1, 1]的。
        if sorted(rank_counts.values()) == cls.rank_counts_benchmark:
            # 获取手牌的所有数值，并按升序排列
            if "A" in ranks:
                card_values_sorted_high = sorted([Card.convertRankToValue(rank=rank, purpose="high") for rank in ranks], reverse=True)
                card_values_sorted_low = sorted([Card.convertRankToValue(rank=rank, purpose="low") for rank in ranks], reverse=True)
                return cls.isContinuous(card_values_sorted_high) or cls.isContinuous(card_values_sorted_low)
            else:
                card_values_sorted = sorted([Card.convertRankToValue(rank=rank) for rank in ranks], reverse=True)
                return cls.isContinuous(card_values_sorted)

        return False

    @classmethod
    def getHandValueHelper(cls, hand: Hand) -> list:
        """
        判断一手符合该牌型的牌的价值序列。

        :param hand: Hand，判定的对象
        :return: a list of the values of the list of cards, from Pattern Value to Major to Minor.
        """
        # 获得手牌的点数
        ranks = hand.getRanks()

        # 分两种情况，有A和没有A的
        if "A" in ranks:
            card_values_sorted_high = sorted([Card.convertRankToValue(rank=rank, purpose="high") for rank in ranks], reverse=True)
            card_values_sorted_low = sorted([Card.convertRankToValue(rank=rank, purpose="low") for rank in ranks], reverse=True)
            if cls.isContinuous(card_values_sorted_high):
                ordered_values = card_values_sorted_high
            else:
                ordered_values = card_values_sorted_low
        else:
            ordered_values = sorted(hand.getValues(purpose="high"), reverse=True)

        return [cls.value] + ordered_values
