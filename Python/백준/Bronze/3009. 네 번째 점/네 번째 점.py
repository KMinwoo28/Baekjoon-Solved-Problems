x_dots = []
y_dots = []

for _ in range(3):
    x, y = map(int, input().split())
    x_dots.append(x)
    y_dots.append(y)

for i in range(3):
    if x_dots.count(x_dots[i]) == 1:
        x4 = x_dots[i]
    if y_dots.count(y_dots[i]) == 1:
        y4 = y_dots[i]

print(x4, y4)