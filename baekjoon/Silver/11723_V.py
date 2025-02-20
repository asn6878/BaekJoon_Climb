import sys
input = sys.stdin.readline

N = int(input())
s = set()

for i in range(N):
    full = input().split()
    if len(full) > 1:
        command, x = full
        x = int(x)
        if command == 'add':
            if not x in s:
                s.add(x)
        elif command == 'remove':
            s.discard(x)
        elif command == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)

    else:
        command = full[0]

        if command == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
