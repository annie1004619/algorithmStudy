from itertools import combinations

def solution(orders, course):
    answer = []
    course_dict ={}
    for order in orders:
        for i in course:
            menu = combinations(sorted(order),i)
            for m in list(menu):
                course_name = ''.join(m)
                if course_name in course_dict:
                    course_dict[course_name] += 1
                else:
                    course_dict[course_name] = 1

    print(course_dict)
    sorted_menu = sorted(course_dict.items(), key=lambda x:[len(x[0]),x[1]], reverse=True)
    length = 0
    max_count = 0

    for name,count in sorted_menu:
        if count < 2:
            continue
        if length != len(name) or max_count == count:
            max_count = count
            length = len(name)
            answer.append(name)

    return sorted(answer)


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

print(solution(orders, course))