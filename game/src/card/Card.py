###################################################
# @project: Texas Hold'em
# @file description: Card class
# @author: Abigail W
# @created on: 2023-09-21
# @last updated: 2023-09-22
###################################################

###################################################
# Import Packages
###################################################
from abc import ABC, abstractmethod


class CardBase(ABC):
    """
    扑克牌的基类
    """

    def __init__(self, suit: str, rank: str):
        self.__suit = suit
        self.__rank = rank

    #######################################################################
    # Getter & Setter methods
    #######################################################################
    @property
    def get_suit(self) -> str:
        return self.__suit

    @property
    def get_rank(self) -> str:
        return self.__rank

    #######################################################################
    # Abstract methods
    #######################################################################
    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def valueOfCard(self, purpose: str) -> int:
        pass

    @abstractmethod
    def compareTo(self, other) -> int:
        pass

    @abstractmethod
    def isSameSuit(self, other) -> bool:
        pass


class Card(CardBase):
    #######################################################################
    # Class attributes
    #######################################################################
    suits = ["♥", "♠", "♦", "♣"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    ranks_order_map = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
        "A": {
            "high": 14,
            "low": 1,
        },
    }

    #######################################################################
    # Default methods
    #######################################################################
    def __init__(self, suit: str, rank: str):
        super().__init__(suit, rank)

    def __str__(self):
        return f"{self.get_suit}{self.get_rank}"

    def __repr__(self):
        return f"{self.get_suit}{self.get_rank}"

    def __eq__(self, other):
        return self.get_suit == other.get_suit and self.get_rank == other.get_rank

    #######################################################################
    # Instance methods
    #######################################################################
    def validate(self) -> bool:
        """
        该方法验证这张牌是否为合法的扑克牌。

        :return:
        """
        return (self.get_suit in self.suits) and (self.get_rank in self.ranks)

    def valueOfCard(self, purpose: str = None) -> int:
        """
        该方法返回这张牌的数值，注意A需要一个purpose参数。

        :param purpose: '对于A的数值是取高还是取低，'high' or 'low'.
        :return: value of the card, in integer.
        """
        if self.get_rank == "A":
            if purpose == "high" or purpose == "low":
                return self.ranks_order_map[self.get_rank][purpose]
            else:
                raise ValueError("输入A时，需要输入purpose参数high或者low.")
        return self.ranks_order_map[self.get_rank]

    def compareTo(self, other: CardBase) -> int:
        """
        该方法将这张牌的点数与另外一张牌的点数进行比较，并返回-1，0，1三种结果。
        -1 代表这张牌的点数 < 另一张牌的点数；
        0 代表这张牌的点数 == 另一张牌的点数；
        1 代表这张牌的点数 > 另一张牌的点数。
        注意此处的隐含假设是因为牌局中通常点数大者为胜，我们default purpose设置为high。

        :param other: 也为Card类型
        :return: int
        """
        value_of_this_card: int = self.valueOfCard(purpose="high")
        value_of_the_other_card: int = other.valueOfCard(purpose="high")
        if value_of_this_card > value_of_the_other_card:
            return 1
        elif value_of_this_card < value_of_the_other_card:
            return -1
        else:
            return 0

    def isSameSuit(self, other: CardBase) -> bool:
        """
        该方法返回这张牌是否和另一张牌为同一花色。
        True 代表是同一花色；
        False 代表不是同一花色。

        :param other: 也为Card类型
        :return: True/False
        """
        return self.get_suit == other.get_suit

    #######################################################################
    # Class methods
    #######################################################################
    @classmethod
    def convertRankToValue(cls, rank: str, purpose: str = "high") -> int:
        """
        该类方法将一个字符串的rank转化为牌的价值value。注意对于A，需要读取一个purpose进行转化。

        :param rank: str, 牌的rank。
        :param purpose: str, "high" or "low".
        :return: int
        """
        if rank in cls.ranks:
            if rank == "A":
                return cls.ranks_order_map["A"][purpose]
            else:
                return cls.ranks_order_map[rank]
        else:
            raise ValueError(f"Rank must fall in the given Poker ranks: {cls.ranks}")

    @classmethod
    def compareValue(cls, first: CardBase, second: CardBase) -> int:
        """
        该方法为静态类方法，用以比较两张卡的点数大小。
        -1 代表first的点数 < second的点数；
        0 代表first的点数 == second的点数；
        1 代表first的点数 > second的点数。

        :param first: Card类型
        :param second: Card类型
        :return: int
        """
        return first.compareTo(other=second)

    @classmethod
    def compareSuit(cls, first: CardBase, second: CardBase) -> bool:
        """
        该方法返回first是否和second为同一花色。
        True 代表是同一花色；
        False 代表不是同一花色。

        :param first:
        :param second:
        :return:
        """
        return first.isSameSuit(second)
