N, B = input().split()

def converter(word):
    if word in "1234567890":
        return int(word)
    else:
        return ord(word) - 55

decimal = 0
B = int(B)
for i in range(len(N)):
    decimal += (converter(N[i]) * (B ** (len(N)-i-1)))
print(decimal)