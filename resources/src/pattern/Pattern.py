###################################################
# @project: Texas Hold'em
# @file description: Pattern base class
# @author: Abigail W
# @created on: 2023-09-22
# @last updated: 2023-11-30
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
from abc import ABC, abstractmethod

# Third-Party Packages
import numpy as np

# Customized Package
from resources.src.card.Card import Card


class Pattern(ABC):
    """
    牌型基类
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = None
    pattern = None
    rank: int = 0

    #######################################################################
    # Class & Abstract methods
    #######################################################################
    @classmethod
    @abstractmethod
    def isInstanceOf(cls, list_of_cards: list[Card]) -> bool:
        """
        该方法判定一手牌是否符合某个牌型，子类必须实现这个方法。

        :param list_of_cards: list[Card]，判定的对象。
        :return: True/False
        """
        pass

    @classmethod
    @abstractmethod
    def getHandValue(cls, list_of_cards: list[Card]) -> np.ndarray:
        """
        判断一手符合该牌型的牌，主要价值为多少。例如，Full House牌型中三条的rank决定了这副牌的主要价值。

        :param list_of_cards: list[Card]，含有5张牌。
        :return: np.ndarray, an array of the values of the list of cards, from Major to Minor.
        """
        pass

    #######################################################################
    # Class methods
    #######################################################################
    @classmethod
    def compareAtoB(cls, A: list[Card], B: list[Card]) -> int:
        """
        该方法将处在同一牌型的一手牌A与另一手牌B进行比较，并返回-1，0，1三种结果。
        -1 代表手牌A的价值 < 手牌B的价值；
        0 代表手牌A的价值   = 手牌B的价值；
        1 代表手牌A的价值   >手牌B的价值。

        :param A: 手牌A
        :param B: 手牌B
        :return: int
        """
        # 判断手牌A和B都为本牌型
        if cls.isInstanceOf(A) and cls.isInstanceOf(B):

            # 获取手牌A和B的major和minor values并进行比对
            values_a, values_b = cls.getHandValue(A), cls.getHandValue(B)

            if values_a[0] > values_b[0]:
                return 1
            elif values_a[0] < values_b[0]:
                return -1
            else:
                if values_a[1] > values_b[1]:
                    return 1
                elif values_a[1] < values_b[1]:
                    return -1
                else:
                    return 0

        elif cls.isInstanceOf(A):
            raise Exception(f"{A} is not a {cls.pattern_name}.")
        elif cls.isInstanceOf(B):
            raise Exception(f"{B} is not a {cls.pattern_name}.")
        else:
            raise Exception(f"{A} and {B} are not a {cls.pattern_name}.")
