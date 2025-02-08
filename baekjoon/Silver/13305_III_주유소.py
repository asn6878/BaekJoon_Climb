n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
answer = 0

for i in range(n - 1):

    if prices[i] < min_price:
        min_price = prices[i]
    answer += min_price * distances[i]

print(answer)