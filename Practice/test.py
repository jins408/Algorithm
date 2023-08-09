burger = [2,1]
temp = []
for i in range(len(burger)-1, -1, -1):
    print(i)
    temp.append(burger[i])
    burger.pop(i)

burger1 = [1,1,2,3,1]
print(burger1[-4:])