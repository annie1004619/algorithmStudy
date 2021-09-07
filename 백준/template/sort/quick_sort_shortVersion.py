array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def qucik_sort(array):
    #리스특 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] #피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x<= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return qucik_sort(left_side) + [pivot] + qucik_sort(right_side)

print(qucik_sort(array))