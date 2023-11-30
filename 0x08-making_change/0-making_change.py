#!/usr/bin/python3
"""a change making module
"""


def makeChange(coins, total):
    """Function shows the fewest num of coins needed 
    for a given amount total given different values.
    """
    if total <= 0:
        return 0
    remain = total
    coin_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remain > 0:
        if coin_index >= n:
            return -1
        if remain - sorted_coins[coin_index] >= 0:
            remain -= sorted_coins[coin_index]
            coin_count += 1
        else:
            coin_index += 1
    return coin_count
