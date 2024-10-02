total = int(input())
bookprice = 0
for _ in range(9):
    bookprice += int(input())
print(total - bookprice)