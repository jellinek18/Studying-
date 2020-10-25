def min_coin_count(value, coin_list):

    sorted_list = sorted(default_coin_list, reverse=True)
    count = 0
    for coin in sorted_list:
        i = value // coin
        count += i
        value = value - coin * i

    return count


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))