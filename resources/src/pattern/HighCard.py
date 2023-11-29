###################################################
# @project: Texas Hold'em
# @file description: High Card Class
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
from resources.src.card.Hand import Hand
from resources.src.pattern.Pattern import Pattern
from resources.src.pattern.Straight import Straight


class HighCard(Pattern, ABC):
    """
    一对牌型
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = "High Card"
    value = 2
    rank_counts_benchmark = [1, 1, 1, 1, 1]

    @classmethod
    def isInstanceOf(cls, list_of_cards: list[Card]) -> bool:
        """
        判断hand是否为一对牌型，是则返回True，否则返回False。

        :param list_of_cards: list[Card]类对象，判定的对象
        :return: True/False
        """
        # 用Counter类型对手牌进行计数
        ranks = [card.get_rank for card in list_of_cards]
        rank_counts = Counter(ranks)

        # 如果计数结果中存在1个rank恰好各有2张牌，另有3张不同rank的牌，则判定为一对
        if sorted(rank_counts.values()) == cls.rank_counts_benchmark and (not Straight.isInstanceOf(list_of_cards)):
            return True

        return False

    @classmethod
    def getHandValue(cls, list_of_cards: list[Card]) -> np.ndarray:
        """
        判断一手符合该牌型的牌的价值序列。

        :param list_of_cards: list[Card]，判定的对象
        :return: np.ndarray, an array of the values of the list of cards, from Major to Minor.
        """
        major_value = max([card.valueOfCard(purpose="high") for card in list_of_cards])
        return np.array([major_value, 0])
