###################################################
# @project: Texas Hold'em
# @file description: Round class, which represents a round of game play
# @author: Abigail W
# @created on: 2023-12-07
# @last updated: 2023-12-08
###################################################

###################################################
# Import Packages
###################################################
# Standard Packages

# Third-Party Packages

# Customized Packages
from game.src.card.Card import Card
from game.src.player.Player import Player


class Round(object):
    """
    德州扑克的单个回合
    """

    def __init__(self, players: list[Player], ) -> None:
        pass