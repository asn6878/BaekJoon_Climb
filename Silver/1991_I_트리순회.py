import sys
input = sys.stdin.readline

nodes = int(input())
li = [list(input().split()) for _ in range(nodes)]
root = li[0][0]
answer = []

def preorder(li, root, nodes): #root = li[0] , nodes = 노드수
    node_value = 0

    if root == '.':
        return
    
    for i in range(len(li)): # 잡아준 루트의 리스트에서의 위치를 찾아주는 함수
        if li[i][0] == root:
            node_value = i
            break

    answer.append(root)
    preorder(li, li[node_value][1], nodes)
    preorder(li, li[node_value][2], nodes)
    return answer

def inorder(li, root, nodes): #root = li[0] , nodes = 노드수
    node_value = 0

    if root == '.':
        return
    
    for i in range(len(li)):
        if li[i][0] == root:
            node_value = i
            break
    
    inorder(li, li[node_value][1], nodes)
    answer.append(root)
    inorder(li, li[node_value][2], nodes)
    return answer

def postorder(li, root, nodes): #root = li[0] , nodes = 노드수
    node_value = 0

    if root == '.':
        return
    
    for i in range(len(li)):
        if li[i][0] == root:
            node_value = i
            break
    
    postorder(li, li[node_value][1], nodes)
    postorder(li, li[node_value][2], nodes)
    answer.append(root)
    return answer 

for i in preorder(li, root, nodes):
    print(i,end='')
print()
answer.clear()

for i in inorder(li, root, nodes):
    print(i,end='')
answer.clear()
print()
for i in postorder(li, root, nodes):
    print(i,end='')