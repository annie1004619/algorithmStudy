from typing import Collection

n,k = map(int, input().split())
people = []
answer = []
index = k-1

for i in range(1, n+1):
    people.append(i)

while people:
    if index >= len(people):
        index %= len(people)

    answer.append(str(people.pop(index)))
    index += k-1

print("<",", ".join(answer),">", sep='')