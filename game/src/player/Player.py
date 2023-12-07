###################################################
# @project: Texas Hold'em
# @file description: Player base class
# @author: Abigail W
# @created on: 2023-12-07
# @last updated: 2023-12-08
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
from abc import ABC, abstractmethod

# Third-Party Packages

# Customized Packages
from game.src.card.Card import Card
# from game.src.card.Hand import Hand
# from game.src.pattern.Pattern import Pattern


class Player(ABC):
    """
    玩家类
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pocket_size = 2

    #######################################################################
    # Default methods
    #######################################################################
    def __init__(self, name: str, initial_balance: float = None) -> None:
        """"""
        self.__name = name
        self.__pocket: list = []
        self.__balance: float = initial_balance
        self.__bet: float = 0
        self.__is_able_to_play: bool = False
        self.__is_in_the_game: bool = False

    #######################################################################
    # Getter & Setter methods
    #######################################################################
    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name) -> None:
        self.__name = new_name

    #######################################################################
    # Instance methods
    #######################################################################
    # Pocket-related methods
    def getPocket(self) -> list[Card]:
        """
        该方法获取玩家的口袋牌。

        :return: 一组口袋牌，list[Card]
        """
        return self.__pocket

    def addCardsToPocket(self, cards: list[Card]) -> None:
        """
        该方法把一组牌添加到self.__pocket中。

        :param cards: 一组牌，一般长度为2。
        :return: None
        """
        self.__pocket.extend(cards)

    def resetPocket(self) -> None:
        """
        该方法重置玩家的口袋。

        :return: None
        """
        self.__pocket = []

    # Balance-related methods
    def getBalance(self) -> float:
        return self.__balance

    def setBalance(self, new_balance: float) -> None:
        self.__balance = new_balance

    def addBalance(self, cash_to_add: float) -> None:
        """
        该方法增加玩家的balance。

        :param cash_to_add: 增加的现金量，float。
        :return: None
        """
        self.__balance += cash_to_add

    def deductBalance(self, cash_to_deduct: float) -> None:
        """
        该方法减少玩家的balance。

        :param cash_to_deduct: 增加的现金量，float。
        :return: None
        """
        self.__balance -= cash_to_deduct

    # Bet-related methods
    def getBet(self) -> float:
        # 返回当前的赌注
        return self.__bet

    def setBet(self, bet) -> None:
        # 设定当前的赌注
        self.__bet = bet

    def resetBet(self) -> None:
        self.__bet = 0

    def addToBet(self, bet: float) -> None:
        self.__bet += bet
        self.deductBalance(bet)

    # Status-related methods
    def getIsAbleToPlay(self) -> bool:
        return self.__is_able_to_play

    def setIsAbleToPlay(self, new_status: bool) -> None:
        self.__is_able_to_play = new_status

    def checkIsAbleToPlay(self, threshold: float = 0) -> None:
        """
        该方法检查玩家是否可以参与游戏，当玩家的balance <= threshold时，不能参与游戏。
        该方法对self.__is_able_to_play进行修改。

        :param threshold: 判断是否可以参加游戏的门槛，默认为0，也可以为大小盲注。
        :return: None
        """
        if self.__balance <= threshold:
            self.__is_able_to_play = False
        else:
            self.__is_able_to_play = True

    def getIsInTheGame(self) -> bool:
        return self.__is_in_the_game

    def setIsInTheGame(self, new_status: bool) -> None:
        self.__is_in_the_game = new_status

    #######################################################################
    # Player actions
    #######################################################################
    def fold(self) -> None:
        """
        该方法执行fold操作，放弃手牌，退出本局游戏，对self.__is_in_the_game进行修改。

        :return: None
        """
        self.resetPocket()
        self.setIsInTheGame(False)

    def makeABet(self, new_bet: float) -> None:
        """
        该方法执行bet操作，下注，对balance和bet进行操作。

        :param new_bet: 新下注的筹码量，float。
        :return:
        """
        if new_bet < 0:
            raise ValueError(f"新下注筹码量为{new_bet}， 下注金额不能为负数。")

        self.deductBalance(new_bet)
        self.addToBet(new_bet)

    def check(self) -> None:
        """
        该方法执行check操作，不下注。

        :return: None
        """
        self.makeABet(0)

    def raiseBet(self, new_target: float, current_price: float) -> None:
        """
        该方法执行raise操作，加注，对balance和bet进行操作。

        :param new_target: 新下注的筹码量，float。
        :param current_price: 当前的赌注，float。
        :return: None
        """
        if new_target <= current_price:
            raise ValueError(f"新下注筹码量为{new_target}， 不能小于等于当前赌注{current_price}。")

        self.makeABet(new_target - current_price)
