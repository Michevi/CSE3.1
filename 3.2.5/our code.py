"""The function move(my_history, their_history) must return "r", "p", or "s".
my_history and their_history are strings of the same length, perhaps length zero.
"""

import random

strategy_name = "Look back 2"


def move(my_history, their_history):
    # first move is always paper
    if (len(their_history) == 0):
        return "p"

    elif(len(their_history) == 1):
        return "r"

    else:
        if their_history[-1] == "p":
            return "s"
        elif their_history[-1] == "r":
            return "p"
        else:
            return "r"