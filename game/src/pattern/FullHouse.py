###################################################
# @project: Texas Hold'em
# @file description: Full House Class
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


class FullHouse(Pattern, ABC):
    """
    葫芦牌型
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = "Full House"
    value = 7
    rank_counts_benchmark = [2, 3]

    @classmethod
    def isInstanceOf(cls, hand: Hand) -> bool:
        """
        判断list_of_cards是否为葫芦牌型，是则返回True，否则返回False。

        :param hand: Hand类对象，判定的对象
        :return: True/False
        """
        # 用Counter类型对手牌进行计数
        ranks = hand.getRanks()
        rank_counts = Counter(ranks)

        # 如果计数结果中存在一个rank恰好有3张牌，另一个rank恰好有2张牌，则判定为葫芦（使用最谨慎的判断方法）
        if sorted(rank_counts.values()) == cls.rank_counts_benchmark:
            return True

        return False

    @classmethod
    def getHandValueHelper(cls, hand: Hand) -> list:
        """
        判断一手符合该牌型的牌的价值序列。

        :param hand: Hand，判定的对象
        :return: a list of the values of the list of cards, from Pattern Value to Major to Minor.
        """
        # 用Counter类型对手牌进行计数
        ranks = hand.getRanks()
        rank_counts = Counter(ranks)

        # 记录手牌的价值
        major_value, minor_value = 0, 0

        for rank, count in rank_counts.items():
            temp = Card.convertRankToValue(rank=rank, purpose="high")
            if count == 3:
                major_value = temp if temp > major_value else major_value
            elif count == 2:
                minor_value = temp if temp > minor_value else minor_value

        return [cls.value, major_value, minor_value]
