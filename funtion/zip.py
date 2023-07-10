# zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고,
# 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환 => 딕셔너리도 가능
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

dic_ex = {}
for a, b in zip(numbers, letters):
    dic_ex[a] = b
print(dic_ex)