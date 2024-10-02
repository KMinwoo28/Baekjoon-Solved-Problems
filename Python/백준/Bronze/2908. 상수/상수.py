a, b = map(str, input().split())
list = []
list.append(int(a[::-1]))
list.append(int(b[::-1]))
print(max(list))