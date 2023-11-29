###################################################
# @project: Texas Hold'em
# @file description: Deck class
# @author: Abigail W
# @created on: 2023-09-21
# @last updated: 2023-09-22
###################################################

###################################################
# Import Packages
###################################################
import numpy as np

# Customized Packages
from resources.src.card.Card import Card


class Deck(object):
    """
    牌堆类
    """

    #######################################################################
    # Class attributes
    #######################################################################

    #######################################################################
    # Initialization
    #######################################################################
    def __init__(self, random_generator=np.random) -> None:
        """
        __init__方法

        :param random_generator: 随机种子生成器，必须有shuffle方法和设置随机种子的set_seed方法。
        """
        self.__deck = []
        self.__random_generator = random_generator
        self.initialize()
        self.shuffle()

    def __str__(self):
        return f"Deck [{self.getLength()} cards left] {self.get_deck}"

    def __repr__(self):
        return f"Deck [{id(self)}] [{self.getLength()} cards left] {self.get_deck}"

    #######################################################################
    # Getter & Setter methods
    #######################################################################
    @property
    def get_deck(self) -> list:
        return self.__deck

    @property
    def get_random_generator(self):
        return self.__random_generator

    def set_deck(self, new_deck: list[Card]) -> None:
        self.__deck = new_deck

    def set_random_generator(self, random_generator) -> None:
        self.__random_generator = random_generator

    #######################################################################
    # Instance methods
    #######################################################################
    def initialize(self) -> None:
        """
        该方法初始化一副去除大小王后数量为52张的扑克牌。

        :return: None
        """
        new_deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                new_deck.append(Card(suit, rank))
        self.set_deck(new_deck=new_deck)

    def getLength(self) -> int:
        """
        该方法获取牌堆剩余扑克牌张数。

        :return: int
        """
        return len(self.get_deck)

    def shuffle(self, seed: int = None) -> None:
        """
        该方法将牌堆洗成随机。

        :param seed: int 随机种子
        :return: None
        """
        if seed:
            self.get_random_generator.seed(seed)
        self.get_random_generator.shuffle(self.get_deck)

    def reset(self) -> None:
        """
        该方法重置牌堆。

        :return: None
        """
        self.initialize()
        self.shuffle()

    def drawCard(self) -> Card:
        """
        该方法抽取牌堆中的一张卡

        :return:
        """
        try:
            return self.get_deck.pop()
        except IndexError:
            print("牌堆中的牌已经发光，将重新洗牌！")
            self.reset()

    def drawNCards(self, n: int) -> list[Card]:
        """
        该方法从牌堆抽取n张扑克牌。若抽取的扑克牌数量大于牌堆剩余的数量，则

        :param n: int 抽取n张扑克牌
        :return: list[Card] 一列表的扑克牌
        """
        if n <= len(self.get_deck):
            return_list = []
            for _ in range(n):
                return_list.append(self.drawCard())
            return return_list
        else:
            print("抽取的扑克牌数量大于牌堆剩余数量！")

    #######################################################################
    # Class methods
    #######################################################################
