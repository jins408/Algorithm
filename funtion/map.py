data = ['3', '2,3', '4,2,3', '2,3,4,1']
numbers = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in data:
    item = list(map(int, item.split(",")))
    print(item, end=" ")

num = list(map(int, numbers))
print(num)

a = ['8','7','3','2','1','1']
print(int(''.join(a)))

'''
def solution(n):
    answer = []

    a = str(n)

    for i in a:
        answer.append(int(i))

    answer.sort(reverse=True)

    b = ''
    for i in answer:
        b += str(i)

    return int(b)
'''
