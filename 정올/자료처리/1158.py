N = int(input())
arr = list(map(int, input().split()))

def insert_sort(N):
  for i in range(1, N) :  #2번째 값부터
    key = arr[i] # i번째 위치의 값을 key로 저장
    j = i - 1 # j를 i 바로 왼쪽 위치로 저장

    while j >= 0 and arr[j] > key:
     arr[j+1] = arr[j]
     j-=1
    arr[j+1] = key
    #찾은 삽입 위치에 key를 저장

    print(' '.join(map(str,arr)))



insert_sort(N)