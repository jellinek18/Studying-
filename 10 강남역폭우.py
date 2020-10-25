def trapping_rain(buildings):
    # 코드를 작성하세요
    total = 0
    count = 0
    for i in range(1, len(buildings) - 1):
            right = max(buildings[:i])
            left = max(buildings[i:])
            yes = min(right, left)
            water = yes - buildings[i]
            total += max(0, water)
    return total

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))