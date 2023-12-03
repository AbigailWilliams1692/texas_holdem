###################################################
# @project: Texas Hold'em
# @file description: Straight Flush Class
# @author: Abigail W
# @created on: 2023-11-23
# @last updated: 2023-11-23
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
from resources.src.card.Hand import Hand
from resources.src.pattern.Pattern import Pattern
from resources.src.pattern.Flush import Flush
from resources.src.pattern.Straight import Straight


class StraightFlush(Pattern, ABC):
    """
    同花顺牌型
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = "Straight Flush"
    value = 9

    @classmethod
    def isInstanceOf(cls, hand: Hand) -> bool:
        """
        判断list_of_card是否为同花顺牌型，是则返回True，否则返回False。

        :param hand: Hand类对象，判定的对象
        :return: True/False
        """
        # 如果手牌既是同花也是顺子，那么判定为同花顺。
        if Flush.isInstanceOf(hand) and Straight.isInstanceOf(hand):
            return True

        return False

    @classmethod
    def getHandValueHelper(cls, hand: Hand) -> np.ndarray:
        """
        判断一手符合该牌型的牌，主要价值为多少。例如，Full House牌型中三条的rank决定了这副牌的主要价值。

        :param hand: Hand类对象，判定的对象
        :return: int, the major value of the list_of_card
        """
        return Straight.getHandValue(hand)
