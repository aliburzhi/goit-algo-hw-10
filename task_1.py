COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in sorted(COINS, reverse=True):
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin

    return dict(sorted(result.items()))
