N = int(input())
T = int(input())
sensors = list(map(int, input().split()))

sensors.sort()
distances = list()

for i in range(1, len(sensors)):
    distances.append(sensors[i] - sensors[i-1])

distances.sort(reverse=True)
answer = sensors[-1] - sensors[0]

for i in range(min(T-1, N-1)):
    answer -= distances[i]

print(answer)