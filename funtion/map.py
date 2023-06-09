data = ['3', '2,3', '4,2,3', '2,3,4,1']
numbers = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in data:
    item = list(map(int, item.split(",")))
    print(item, end=" ")

num = list(map(int, numbers))
print(num)