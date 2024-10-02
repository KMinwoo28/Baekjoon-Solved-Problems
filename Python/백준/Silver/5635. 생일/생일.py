P = int(input())
people = []
for _ in range(P): 
    people.append(list(map(str, input().split())))
for i in range(P):
    people[i][1],people[i][2],people[i][3] = int(people[i][1]), int(people[i][2]), int(people[i][3])
people.sort(key = lambda x:(x[3], x[2], x[1]), reverse = True)
print(people[0][0])
print(people[-1][0])