###################################################
# @project: Texas Hold'em
# @file description: Hand class
# @author: Abigail W
# @created on: 2023-09-22
# @last updated: 2023-09-22
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages


# Third-Party Packages

# Customized Packages
from game.src.card.Card import Card


class Hand:
    """
    代表一手牌（共X张）类
    """

    #######################################################################
    # Class attributes
    #######################################################################
    __size = 5

    ######################################################################
    # Class methods
    #######################################################################
    @classmethod
    def setHandSize(cls, new_hand_size: int):
        cls.__size = new_hand_size

    #######################################################################
    # Initialization
    #######################################################################
    def __init__(self, cards: list[Card]) -> None:
        assert self.get_size == len(cards), f"手牌数量错误！设置数量为{self.get_size}张，输入数量为{len(cards)}张。"
        self.__cards = cards
        self.__pattern = None

    def __str__(self):
        return f"Hand [{self.get_size} cards] {self.get_cards}"

    def __repr__(self):
        return f"Hand [{id(self)}] [{self.get_size} cards] {self.get_cards}"

    def __len__(self):
        return len(self.get_cards)

    #######################################################################
    # Getter & Setter methods
    #######################################################################
    @property
    def get_cards(self) -> list[Card]:
        return self.__cards

    def set_cards(self, new_cards: list[Card]) -> None:
        assert self.get_size == len(new_cards), f"手牌长度错误！设置长度为{self.get_size}，输入长度为{len(new_cards)}。"
        self.__cards = new_cards

    @property
    def get_size(self) -> int:
        return self.__size

    #######################################################################
    # Instance methods
    #######################################################################
    def getCard(self, pos: int) -> Card:
        """
        根据所给的位置获取一手牌中的扑克牌。

        :param pos: int 位置参数
        :return: Card类
        """
        return self.get_cards[pos]

    def getRanks(self) -> list[str]:
        """
        获取一手牌的所有ranks。

        :return: 一手牌的所有ranks，a list of strings.
        """
        return [card.get_rank for card in self.get_cards]

    def getSuits(self) -> list[str]:
        """
        获取一手牌的所有花色suits。

        :return: 一手牌的所有suits，a list of strings.
        """
        return [card.get_suit for card in self.get_cards]

    def getValues(self, purpose: str = None) -> list[int]:
        """
        获取一手牌的所有数值，注意A的数值取决于purpose。

        :param purpose: 对于A的数值是取高还是取低，'high' or 'low'.
        :return: value of the cards in a hand, a list of integers
        """
        return [card.valueOfCard(purpose=purpose) for card in self.get_cards]
