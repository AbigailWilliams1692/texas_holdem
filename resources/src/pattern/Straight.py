###################################################
# @project: Texas Hold'em
# @file description: Straight class
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
import numpy as np

# Customized Packages
from resources.src.card.Card import Card
from resources.src.pattern.Pattern import Pattern


class Straight(Pattern, ABC):
    """
    顺子牌型
    """

    #######################################################################
    # Class attributes
    #######################################################################
    pattern_name = "Straight"
    value = 5
    rank_counts_benchmark = [1, 1, 1, 1, 1]

    @staticmethod
    def isContinuous(arr: list[int]) -> bool:
        """
        辅助函数，以测试一列升序整数是否连续（间隔为1）。

        :param arr: a list of increasing integers with interval 1.
        :return: True or False
        """
        return all([(arr[i] + 1) == arr[i + 1] for i in range(len(arr) - 1)])

    @classmethod
    def isInstanceOf(cls, list_of_cards: list[Card]) -> bool:
        """
        判断list_of_cards是否为顺子牌型，是则返回True，否则返回False。

        :param list_of_cards: list[Card]类对象，判定的对象
        :return: True/False
        """
        # 获取手牌的所有ranks
        ranks = [card.get_rank for card in list_of_cards]

        # 用Counter类型对手牌进行计数
        rank_counts = Counter(ranks)

        # 首先排除任何Counter.values()不是[1, 1, 1, 1, 1]的。
        if sorted(rank_counts.values()) == cls.rank_counts_benchmark:
            # 获取手牌的所有数值，并按升序排列
            if "A" in ranks:
                card_values_sorted_high = sorted([Card.convertRankToValue(rank=rank, purpose="high") for rank in ranks])
                card_values_sorted_low = sorted([Card.convertRankToValue(rank=rank, purpose="low") for rank in ranks])
                return cls.isContinuous(card_values_sorted_high) or cls.isContinuous(card_values_sorted_low)
            else:
                card_values_sorted = sorted([Card.convertRankToValue(rank=rank) for rank in ranks])
                return cls.isContinuous(card_values_sorted)

        return False

    @classmethod
    def getHandValue(cls, list_of_cards: list[Card]) -> np.ndarray:
        """
        判断一手符合该牌型的牌的价值序列。

        :param list_of_cards: list[Card]，判定的对象
        :return: np.ndarray, an array of the values of the list of cards, from Major to Minor.
        """
        # 获得手牌的点数
        ranks = [card.get_rank for card in list_of_cards]

        # 分两种情况，有A和没有A的
        if "A" in ranks:
            card_values_sorted_high = sorted([Card.convertRankToValue(rank=rank, purpose="high") for rank in ranks])
            card_values_sorted_low = sorted([Card.convertRankToValue(rank=rank, purpose="low") for rank in ranks])
            if cls.isContinuous(card_values_sorted_high):
                major_value = max(card_values_sorted_high)
            else:
                major_value = max(card_values_sorted_low)
        else:
            major_value = max([card.valueOfCard(purpose="high") for card in list_of_cards])

        return np.array([major_value, 0])


if __name__ == "__main__":
    print("Test isContinuous")
    lst = [1, 2, 3, 4, 5]
    print(f"Is the list continuous? Answer: {Straight.isContinuous(lst)}")

    print()

    print("Initializing a list of cards of cards...")
    list_of_cards1 = [Card("♥", "A"), Card("♦", "J"), Card("♠", "Q"), Card("♣", "10"), Card("♥", "K")]
    print(list_of_cards1)
    print("Is this list of cards a Straight?")
    is_four_of_a_kind1 = Straight.isInstanceOf(list_of_cards=list_of_cards1)
    print(f"Answer is {'Yes' if is_four_of_a_kind1 else 'No'}.")

    print()

    print("Initializing a list_of_cards of cards...")
    list_of_cards2 = [Card("♥", "A"), Card("♦", "2"), Card("♠", "3"), Card("♣", "4"), Card("♥", "5")]
    print(list_of_cards2)
    print("Is this list of cards a Straight?")
    is_four_of_a_kind2 = Straight.isInstanceOf(list_of_cards=list_of_cards2)
    print(f"Answer is {'Yes' if is_four_of_a_kind2 else 'No'}.")

    print()

    print("Initializing a list of cards of cards...")
    list_of_cards3 = [Card("♥", "7"), Card("♦", "8"), Card("♠", "9"), Card("♣", "10"), Card("♥", "J")]
    print(list_of_cards3)
    print("Is this list of cards a Straight?")
    is_four_of_a_kind3 = Straight.isInstanceOf(list_of_cards=list_of_cards3)
    print(f"Answer is {'Yes' if is_four_of_a_kind3 else 'No'}.")

    print()

    print("Initializing a list of cards of cards...")
    list_of_cards4 = [Card("♥", "7"), Card("♥", "10"), Card("♥", "9"), Card("♥", "10"), Card("♥", "J")]
    print(list_of_cards4)
    print("Is this list of cards a Straight?")
    is_four_of_a_kind4 = Straight.isInstanceOf(list_of_cards=list_of_cards4)
    print(f"Answer is {'Yes' if is_four_of_a_kind4 else 'No'}.")
