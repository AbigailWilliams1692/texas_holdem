###################################################
# @project: Texas Hold'em
# @file description: Pattern base class
# @author: Abigail W
# @created on: 2023-09-22
# @last updated: 2023-12-06
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
from abc import ABC, abstractmethod

# Third-Party Packages
import numpy as np

# Customized Package
from game.src.card.Hand import Hand


class Pattern(ABC):
    """
    牌型基类
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = None
    pattern = None
    value = 0

    #######################################################################
    # Class & Abstract methods
    #######################################################################
    @classmethod
    @abstractmethod
    def isInstanceOf(cls, hand: Hand) -> bool:
        """
        该方法判定一手牌是否符合某个牌型，子类必须实现这个方法。

        :param hand: Hand，判定的对象。
        :return: True/False
        """
        pass

    @classmethod
    @abstractmethod
    def getHandValueHelper(cls, hand: Hand) -> list:
        """
        该方法为Helper方法。
        判断一手符合该牌型的牌，主要价值为多少。例如，Full House牌型中三条的rank决定了这副牌的主要价值。

        :param hand: Hand，含有5张牌。
        :return: a dictionary of the values of the list of cards, from Major to Minor.
        """
        pass

    #######################################################################
    # Class methods
    #######################################################################
    @classmethod
    def getHandValue(cls, hand: Hand) -> list:
        """
        判断一手符合该牌型的牌，主要价值为多少。例如，Full House牌型中三条的rank决定了这副牌的主要价值。

        :param hand: Hand，含有5张牌。
        :return: a dictionary of the values of the list of cards, from Pattern Value to Major to Minor.
        """
        if cls.isInstanceOf(hand):
            return cls.getHandValueHelper(hand)
        else:
            raise TypeError(f"{hand} 不属于牌型{cls.pattern_name}!")

    @classmethod
    def getPatternName(cls) -> str:
        """
        该方法获取牌型的名称。

        :return: 牌型名称，str。
        """
        return cls.pattern_name

    @classmethod
    def getPatternValue(cls) -> int:
        """
        该方法获取牌型的价值。

        :return: 牌型价值，int。
        """
        return cls.value
