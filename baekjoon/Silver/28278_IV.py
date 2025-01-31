import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return 1
        
        return 0

    def peek(self):
        if len(self.stack) == 0:
            return -1
        
        return self.stack[-1]


stack = Stack()
count = int(input())
commands = list()
results = []

for _ in range(count):
    n = input().strip()
    commands.append(n)

for command in commands:
    n = command.split()
    if n[0] == "1":
        stack.push(int(n[1]))
    elif n[0] == "2":
        print(stack.pop())
    elif n[0] == "3":
        print(stack.size())
    elif n[0] == "4":
        print(stack.isEmpty())
    elif n[0] == "5":
        print(stack.peek())