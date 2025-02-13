N = int(input())
sizes = list(map(int, input().split()))
Sm, Pm = list(map(int, input().split()))

T = 0
for i in sizes:
    tmp = i // Sm
    if i % Sm == 0:
        T += tmp
    else:
        T += tmp + 1

Pq = N // Pm
Pr = N % Pm
print(T)
print(Pq, Pr)