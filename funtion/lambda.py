# 일반함수
def is_even(x):
  return x % 2 == 0
# 람다
s_even = lambda x : x % 2 == 0

print(is_even(1)) # False
print(is_even(2)) # True


# 1. 일반 함수 버전
def plus_two(x):
    return x + 2

result1 = list(map(plus_two, [1, 2, 3, 4, 5]))
print(result1)

# 2.  람다 함수 버전
result2 = list(map((lambda x: x + 2), [1, 2, 3, 4, 5]))
print(result2)

#sorted

a = [ (1,2), (0,1), (5,1), (5,2), (3,0)]


b = sorted(a)
print(b)
# sorted(a,key=lambda x:x[0])
c = sorted(a, key=lambda x: x[0])
print(c)
d = sorted(a, key=lambda x: x[1])
print(d)

def soultion(n):
    arr = n
    arr = sorted(arr, key=lambda x:len(x))
    print(arr)
    return

arr = ['1.2,3', '1', '4,3', '3,5']

print(soultion(arr))
