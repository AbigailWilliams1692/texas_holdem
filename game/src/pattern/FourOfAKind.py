###################################################
# @project: Texas Hold'em
# @file description: Four of a Kind class
# @author: Abigail W
# @created on: 2023-09-21
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


class FourOfAKind(Pattern, ABC):
    """
    四条牌型
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = "Four of a Kind"
    value = 8
    rank_counts_benchmark = [1, 4]

    @classmethod
    def isInstanceOf(cls, hand: Hand) -> bool:
        """
        判断list_of_cards是否为四条牌型，是则返回True，否则返回False。

        :param hand: Hand，判定的对象
        :return: True/False
        """
        # 用Counter类型对手牌进行计数
        ranks = hand.getRanks()
        rank_counts = Counter(ranks)

        # 如果计数结果中存在一个rank恰好有4张牌，则判定是四条（使用最谨慎的判断方法）
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
            if count == 4:
                major_value = temp if temp > major_value else major_value
            elif count == 1:
                minor_value = temp if temp > minor_value else minor_value

        return [cls.value, major_value, minor_value]
