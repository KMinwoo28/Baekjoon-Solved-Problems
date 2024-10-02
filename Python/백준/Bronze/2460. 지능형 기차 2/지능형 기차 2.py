max = 0
people = 0
for _ in range(10):
    o, i = map(int,input().split())
    people = people - o + i
    if max < people:
        max = people
print(max)