###################################################
# @project: Texas Hold'em
# @file description: Texas Deck class
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


class TexasDeck(object):
    """
    牌堆类
    """

    #######################################################################
    # Class attributes
    #######################################################################
    number_of_cards_in_a_deck = 52

    #######################################################################
    # Initialization
    #######################################################################
    def __init__(self, random_generator=np.random, list_of_cards: list[Card] = None) -> None:
        """
        __init__方法

        :param random_generator: 随机种子生成器，必须有shuffle方法和设置随机种子的set_seed方法。
        """
        self.__deck = list_of_cards if list_of_cards else []
        self.__random_generator = random_generator
        if not self.__deck:
            self.initialize()
            self.shuffle()

    def __str__(self):
        return f"Deck [{self.getLength()} cards left] {self.get_deck}"

    def __repr__(self):
        return f"Deck [{id(self)}] [{self.getLength()} cards left] {self.get_deck}"

    def __eq__(self, other):
        if self.getLength() == other.getLength() and self.get_random_generator == other.get_random_generator:
            for i in range(self.getLength()):
                if self.getCard(i) != other.getCard(i):
                    return False
        return True

    #######################################################################
    # Getter & Setter methods
    #######################################################################
    @property
    def get_deck(self) -> list:
        return self.__deck

    @property
    def get_random_generator(self):
        return self.__random_generator

    def getLength(self) -> int:
        """
        该方法获取牌堆剩余扑克牌张数。

        :return: int
        """
        return len(self.get_deck)

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

    def validateEachCard(self) -> bool:
        """
        该方法验证这幅扑克牌是否每一张牌都合法。

        :return: True/False
        """
        return all([card.validate() for card in self.get_deck])

    def validateWhole(self) -> bool:
        """
        该方法验证这副扑克牌是否整体合法，与出厂无异。

        :return: True/False
        """
        # 检查一共有52张牌
        is_number_correct = (self.getLength() == self.number_of_cards_in_a_deck)
        # 检查每张牌都合规
        is_each_card_valid = [card.validate() for card in self.get_deck]
        # 检查没有重复的牌
        is_each_card_in_deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                is_each_card_in_deck.append(Card(suit, rank) in self.get_deck)
        return is_number_correct and all(is_each_card_valid) and all(is_each_card_in_deck)

    def getCard(self, pos: int) -> Card:
        """
        该方法将获取牌堆中的第pos张牌。

        :param pos: 扑克牌的位置序数，0<= pos < self.getLength()
        :return: Card: 那一张扑克牌
        """
        if isinstance(pos, int) and 0 <= pos < self.getLength():
            return self.get_deck[pos]
        else:
            raise ValueError("使用getCard方法获取第x张牌时，x必须为非负整数，且小于牌堆的总数。")

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

    def copy(self):
        """
        该方法会复制一份当前的牌组，两者会拥有相同的属性，但牌堆指向不同的内存地址。

        :return:Deck: 一份当前牌组的复制品。
        """
        new_deck = TexasDeck(random_generator=self.get_random_generator)
        new_deck.set_deck(self.get_deck.copy())
        return new_deck

    def drawCard(self) -> Card | None:
        """
        该方法抽取牌堆中的一张卡

        :return:
        """
        try:
            return self.get_deck.pop()
        except IndexError:
            # print("牌堆中的牌已经发光")
            return None

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
            raise ValueError("抽取的扑克牌数量大于牌堆剩余数量！")

    #######################################################################
    # Class methods
    #######################################################################
