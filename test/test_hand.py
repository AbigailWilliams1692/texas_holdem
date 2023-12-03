###################################################
# @project: Texas Hold'em
# @file description: Test Hand Class
# @author: Abigail W
# @created on: 2023-12-02
# @last updated: 2023-12-02
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages
import unittest

# Third-Party Packages

# Customized Packages
from resources.src.card.Card import Card
from resources.src.card.Hand import Hand


class TestingHand(unittest.TestCase):
    """
    测试手牌类
    """

    def test_hand_size(self):
        # 测试默认手牌数量为5张
        self.assertEqual(Hand.get_size, 5)

    def test_set_size(self):
        # 测试修改手牌数量为6张
        Hand.setHandSize(6)
        self.assertEqual(Hand.get_size, 6)
        Hand.setHandSize(5)

    def test_set_up(self):
        # 测试创建手牌对象
        hand1 = Hand([Card("♣", "9"), Card("♥", "8"), Card("♦", "10"), Card("♠", "J"), Card("♣", "Q")])
        self.assertEqual(str(hand1),
                         f"Hand [5 cards] {[Card('♣', '9'), Card('♥', '8'), Card('♦', '10'), Card('♠', 'J'), Card('♣', 'Q')]}")
        self.assertRaises(AssertionError, Hand, [Card("♣", "9"), Card("♥", "8"), Card("♦", "10"), Card("♠", "J")])

    def test_getter_and_setter(self):
        # 测试Getter and Setter方法
        hand1 = Hand([Card("♣", "9"), Card("♥", "8"), Card("♦", "10"), Card("♠", "J"), Card("♣", "Q")])
        self.assertEqual(hand1.get_cards,
                         [Card("♣", "9"), Card("♥", "8"), Card("♦", "10"), Card("♠", "J"), Card("♣", "Q")])
        hand1.set_cards([Card("♣", "Q"), Card("♥", "Q"), Card("♦", "Q"), Card("♠", "2"), Card("♣", "2")])
        self.assertEqual(hand1.get_cards,
                         [Card("♣", "Q"), Card("♥", "Q"), Card("♦", "Q"), Card("♠", "2"), Card("♣", "2")])

    def test_get_card(self):
        # 测试getCard方法
        list_of_cards = [Card("♣", "9"), Card("♥", "8"), Card("♦", "10"), Card("♠", "J"), Card("♣", "Q")]
        hand1 = Hand(cards=list_of_cards)
        for i in range(len(hand1)):
            self.assertEqual(hand1.getCard(i), list_of_cards[i])

    def test_get_ranks(self):
        # 测试getRanks方法
        list_of_cards = [Card("♣", "9"), Card("♥", "8"), Card("♦", "10"), Card("♠", "J"), Card("♣", "Q")]
        hand1 = Hand(cards=list_of_cards)
        self.assertEqual(hand1.getRanks(), [hand1.getCard(i).get_rank for i in range(len(hand1))])

    def test_get_suits(self):
        # 测试getSuits方法
        list_of_cards = [Card("♣", "9"), Card("♥", "8"), Card("♦", "10"), Card("♠", "J"), Card("♣", "Q")]
        hand1 = Hand(cards=list_of_cards)
        self.assertEqual(hand1.getSuits(), [hand1.getCard(i).get_suit for i in range(len(hand1))])

    def test_get_values(self):
        # 测试getValues方法
        list_of_cards1 = [Card("♣", "9"), Card("♥", "8"), Card("♦", "10"), Card("♠", "J"), Card("♣", "Q")]
        hand1 = Hand(cards=list_of_cards1)
        self.assertEqual(hand1.getValues(), [hand1.getCard(i).valueOfCard() for i in range(len(hand1))])
        list_of_cards2 = [Card("♣", "A"), Card("♥", "2"), Card("♦", "3"), Card("♠", "4"), Card("♣", "5")]
        hand2 = Hand(cards=list_of_cards2)
        self.assertEqual(hand2.getValues(purpose="low"), [1, 2, 3, 4, 5])
        list_of_cards3 = [Card("♣", "10"), Card("♥", "J"), Card("♦", "Q"), Card("♠", "K"), Card("♣", "A")]
        hand3 = Hand(cards=list_of_cards3)
        self.assertEqual(hand3.getValues(purpose="high"), [10, 11, 12, 13, 14])

    def test_calculate_pattern(self):
        pass
