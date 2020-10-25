def course_selection(course_list):
    sorted_list = sorted(course_list, key=lambda x: x[1])

    my_selection = [sorted_list[0]]

    for course in sorted_list:
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)

    return my_selection

print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 6), (13, 16), (9, 11), (1, 8)]))
