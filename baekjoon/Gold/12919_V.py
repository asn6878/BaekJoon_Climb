import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()
answer = 0
visited = set()

def sol(word):
    global answer
    if answer == 1:
        return

    if len(word) < len(S):
        return
    
    if word == S:
        answer = 1
        return
    
    visited.add(word)

    if word[-1] == 'A':
        current = word[0:-1]
        if not current in visited:
            sol(current)
    
    if word[0] == 'B':
        current = word[1:][::-1]
        if not current in visited:
            sol(current)

sol(T)
print(visited)
print(answer)