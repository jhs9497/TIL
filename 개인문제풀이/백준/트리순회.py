N = int(input())

tree = {}
for i in range(N):
    root, L, R = list(input().split())
    tree[root] =[L, R]

def preorder(root):
    global preorder_result
    preorder_result += root
    if tree[root][0] != '.':
        preorder(tree[root][0])
    if tree[root][1] != '.':
        preorder(tree[root][1])

def inorder(root):
    global inorder_result
    if tree[root][0] != '.':
        inorder(tree[root][0])
    inorder_result += root
    if tree[root][1] != '.':
        inorder(tree[root][1])

def postorder(root):
    global postorder_result
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    postorder_result += root


preorder_result = ''
inorder_result = ''
postorder_result = ''

preorder('A')
inorder('A')
postorder('A')

print(tree)
print(preorder_result)
print(inorder_result)
print(postorder_result)
