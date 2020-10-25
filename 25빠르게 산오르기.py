def select_stops(water_stops, capacity):

    stops = []

    prev_stop = 0

    for i in range(len(water_stops)):

        if water_stops[i] - prev_stop > capacity:
            stops.append(water_stops[i-1])
            prev_stop = water_stops[i - 1]

    stops.append(water_stops[-1])

    return stops





# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))