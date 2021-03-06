import sys

stack = []

def push(input):
    stack.append(input)

def empty():
    print(1 if size() == 0 else 0) 

def pop():
    try:
        print(stack.pop())
    except:
        print('-1')

def size():
    return len(stack)

def top():
    try:
        print(stack[-1])
    except:
        print('-1')
        
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        push(cmd[1])

    elif cmd[0] == 'pop':
        pop()

    elif cmd[0] == 'empty':
        empty()

    elif cmd[0] == 'size':
        print(size())

    elif cmd[0] == 'top':
        top()