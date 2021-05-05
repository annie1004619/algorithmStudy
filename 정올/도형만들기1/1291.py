s, e = map(int, input().split())

while (s not in range(2,10)) or (e not in range(2,10)):
  print('INPUT ERROR!')
  s, e = map(int, input().split())

if(s <= e):
  for i in range(1, 10):
    for j in range(s, e+1):
      print(j, '*', i, '=', str(i*j).rjust(2), end="   ")
    print('')


if(s > e):
    for i in range(1, 10):
      for j in range(s, e-1, -1):
        print(j, '*', i, '=', str(i*j).rjust(2), end="   ")
      print('')