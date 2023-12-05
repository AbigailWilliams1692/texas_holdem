###################################################
# @project: Texas Hold'em
# @file description: Flush Class
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
from game.src.card.Hand import Hand
from game.src.pattern.Pattern import Pattern


class Flush(Pattern, ABC):
    """
    同花牌型
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = "Flush"
    value = 6
    suit_counts_benchmark = [5]

    @classmethod
    def isInstanceOf(cls, hand: Hand) -> bool:
        """
        判断list_of_cards是否为同花牌型，是则返回True，否则返回False。

        :param hand: Hand类对象，判定的对象
        :return: True/False
        """
        # 用Counter类型对手牌花色进行计数
        suits = hand.getSuits()
        suit_counts = Counter(suits)

        # 如果计数结果中存在一个suit有5张牌（使用最谨慎的判断方法）
        if sorted(suit_counts.values()) == cls.suit_counts_benchmark:
            return True

        return False

    @classmethod
    def getHandValueHelper(cls, hand: Hand) -> list:
        """
        判断一手符合该牌型的牌的价值序列。

        :param hand: Hand，判定的对象
        :return: a list of te values of the cards,
        """
        ordered_values = sorted(hand.getValues(purpose="high"), reverse=True)
        return [cls.value] + ordered_values
