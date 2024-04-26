"""The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
"""

import random

strategy_name = "cutting the paper"

def beat_move(move):
    if (move=="r"):
        return "p"
    if (move == "p"):
        return "s"
    if (move=="s"):
        return "r"

def move(my_history, their_history):
    """This player always starts with rock
    """
    if (len(their_history) < 2):
        return "p"
    if (their_history[-2] == their_history[-1]):
        return beat_move(their_history[-2])

    if (len(their_history) < 7):
        return "s"
    if (their_history[-6] == their_history[-5]):
        return beat_move(their_history[-3])

    return random.choice(["r", "p", "s"])




