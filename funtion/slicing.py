arr = ['a','b','c','d','e']

# 특정시작위치부터 끝까지 가져오기
print(arr[1:])

# 시작점부터 특정 위치까지 가져오기
print(arr[:3])
print(arr[:-1])

#특정 위치부터 특정 위치까지 모두 가져오기
print(arr[1:4])
print(arr[-4:-2])
print("-------------")
print(arr[2:4])

# 2칸씩 이동하면서 가져옵니다.
print(arr[::2])
print(arr[::3])

# 전체를 거꾸로 가져옵니다.
print(arr[::-1])
print("#############")
print(arr[1::2])

s = "aa.bb.cc.BlockDMask.ee.ff.gg.python.example"
print(f'{s}')

r0 = s.split('.')
r1 = s.split('.', 3)
r2 = s.split(sep='.', maxsplit=2)
r3 = s.split('.', maxsplit=3)
print(r0)
print(r1)
print(r2)
print(r3)