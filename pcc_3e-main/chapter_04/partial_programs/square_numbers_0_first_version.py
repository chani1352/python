squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(type(squares))
print(squares)

for i,v in enumerate(squares):
    print("{}는 {}".format(i,v))