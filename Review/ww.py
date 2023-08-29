def solution(n, t, m, p):
    result = "0"

    for num in range(1, t * m):
        result += radix_transformation(n, num)
    print(result)

    return "".join(result[idx] for idx in range(p - 1, t * m, m))


def radix_transformation(base: int, number: int) -> str:
    result = ""

    while number != 0:
        number, mod = divmod(number, base)

        if base > 10 and (10 <= mod <= 15):
            result += "ABCDEF"[mod % 10]
        else:
            result += str(mod)

    return result[::-1]
n=16
t=16
m=2
p=1
print(solution(n,t,m,p))
#123456789ABCDEF101112131415161718191A1B1C1D1E1F
#13579BDF01234567

#0123456789ABCDEF101112131415161718191A1B1C1D1E1F
#02468ACE11111111