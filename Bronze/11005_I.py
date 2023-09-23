def dton(num: int):
    if num < 10:
        return str(num)
    return chr(num + 55)

def converter(n: int, x: int):
    result = []
    while n > 0:
        remainder = n % x
        result.append(dton(remainder))
        n //= x
    return ''.join(result[::-1])

n, x = map(int, input().split())
result = converter(n, x)
print(result)