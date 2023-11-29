###################################################
# @project: Texas Hold'em
# @file description: Two Pairs Class
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
from resources.src.card.Card import Card
from resources.src.pattern.Pattern import Pattern


class TwoPairs(Pattern, ABC):
    """
    两对牌型
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = "Two Pairs"
    value = 3
    rank_counts_benchmark = [1, 1, 2]

    @classmethod
    def isInstanceOf(cls, list_of_cards: list[Card]) -> bool:
        """
        判断list_of_cards是否为两对牌型，是则返回True，否则返回False。

        :param list_of_cards: list[Card]类对象，判定的对象
        :return: True/False
        """
        # 用Counter类型对手牌进行计数
        ranks = [card.get_rank for card in list_of_cards]
        rank_counts = Counter(ranks)

        # 如果计数结果中存在2个rank恰好各有2张牌，另有1张不同rank的牌，则判定为两对
        if sorted(rank_counts.values()) == cls.rank_counts_benchmark:
            return True

        return False

    @classmethod
    def getHandValue(cls, list_of_cards: list[Card]) -> np.ndarray:
        """
        判断一手符合该牌型的牌的价值序列。

        :param list_of_cards: list[Card]，判定的对象
        :return: np.ndarray, an array of the values of the list of cards, from Major to Minor.
        """
        # 用Counter类型对手牌进行计数
        ranks = [card.get_rank for card in list_of_cards]
        rank_counts = Counter(ranks)

        # 记录手牌的价值
        major_value, minor_value = 0, 0

        for rank, count in rank_counts.items():
            temp = Card.convertRankToValue(rank=rank, purpose="high")
            if count == 2:
                major_value = temp if temp > major_value else major_value
            elif count == 1:
                minor_value = temp if temp > minor_value else minor_value

        return np.array([major_value, minor_value])
