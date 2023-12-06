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

# Customized Packages
from game.src.card.Card import Card
from game.src.card.Hand import Hand
from game.src.pattern.Pattern import Pattern


class TwoPairs(Pattern, ABC):
    """
    两对牌型
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = "Two Pairs"
    value = 3
    rank_counts_benchmark = [1, 2, 2]

    @classmethod
    def isInstanceOf(cls, hand: Hand) -> bool:
        """
        判断list_of_cards是否为两对牌型，是则返回True，否则返回False。

        :param hand: Hand类对象，判定的对象
        :return: True/False
        """
        # 用Counter类型对手牌进行计数
        ranks = hand.getRanks()
        rank_counts = Counter(ranks)

        # 如果计数结果中存在2个rank恰好各有2张牌，另有1张不同rank的牌，则判定为两对
        if sorted(rank_counts.values()) == cls.rank_counts_benchmark:
            return True

        return False

    @classmethod
    def getHandValueHelper(cls, hand: Hand) -> list:
        """
        判断一手符合该牌型的牌的价值序列。

        :param hand: Hand，判定的对象
        :return: a list of the values of the list of cards, from Major to Minor.
        """
        # 用Counter类型对手牌进行计数
        ranks = hand.getRanks()
        rank_counts = Counter(ranks)

        # 记录手牌的价值
        major_values, minor_values = [], []

        for rank, count in rank_counts.items():
            temp = Card.convertRankToValue(rank=rank, purpose="high")
            if count == 2:
                major_values.append(temp)
            else:
                minor_values.append(temp)

        return [cls.value] + sorted(major_values, reverse=True) + minor_values
