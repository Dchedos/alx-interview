#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    """This function will take a list of coins and use
       that to calculate how much change the total will require
    """
    if total <= 0:
        return 0
    """
    Initialize an array to store the minimum number of coins
    needed for each value
    """
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[total] == sys.maxsize:
        return -1
    return dp[total]
