people = 0
max_p = 0
for i in range(4):
    o, i = map(int,input().split())
    people = people - o + i
    if max_p < people:
        max_p = people
print(max_p)