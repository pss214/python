     
class MinHeap :               
    def __init__ (self) :      
        self.heap = []         
        self.heap.append(0)      

    def size(self) : return len(self.heap) - 1   
    def isEmpty(self) : return self.size() == 0   
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]   
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = '힙 트리: ') :
        print(msg, self.heap[1:])   

    def insert(self, n) :
        self.heap.append(n)      
        i = self.size()         
        while (i != 1 and n < self.Parent(i)): 
            self.heap[i] = self.Parent(i)      
            i = i // 2                        
        self.heap[i] = n                    

    def delete(self) :
        parent = 1
        child = 2
        if not self.isEmpty() :
            hroot = self.heap[1]          
            last = self.heap[self.size()]   
            while (child <= self.size()):   
                if child<self.size() and self.Left(parent)>self.Right(parent):
                    child += 1
                if last <= self.heap[child] :       
                    break;                          
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last   
            self.heap.pop(-1)          
            return hroot
def make_tree(freq):
    heap = MinHeap()
    for n in freq :
        heap.insert(n)

    for i in range(0, n) :
        e1 = heap.delete()
        e2 = heap.delete()
        heap.insert(e1 + e2)
        print(" (%d+%d)" % (e1, e2))
'''
label = [ 'E', 'T', 'N', 'I', 'S' ]
freq  = [15, 12, 8, 6, 4 ]
make_tree(freq)
'''



class BSTNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
     
def search_bst(n,key):
    if n is None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)
def search_bst_iter(n,key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n=n.right
    return None
def search_value_bst(n,value):
    if n == None : return None
    elif value == n.value: 
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)
def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n
def search_min_bst(n):
    while n != None and n.left != None:
        n= n.left
    return n
def insert_bst(r,n):
    if n.key < r.key:
        if r.right is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False
def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root
def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root
def delete_bst_case3(node, root):
    succp = node
    succ = node.right
    while succ.left != None:
        succp = succ
        succ = succ.left
    if succp.left == succ:
        succp.left = succ.right
    else:
        succp.right = succ.right
    node.key = succ.key
    node.value = succ.value

    return root
def delete_bst(root : BSTNode,key):
    if root == None: return None

    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key : node = node.left
        else : node = node.right
    if node == None : return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent,node,root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent,node,root)
    else:
        root = delete_bst_case3(node,root)
    return root
def count_node(n) :
    node = n.root
    if node is None:
        return 0
    stack = []
    stack.append(node)
    cnt = 0
    while stack:
        cnt += 1
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return cnt
def inorder(n):
    if n is None:
        return
class BSTMap:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    def clear(self):
        self.root = None
    def size(self):
        return count_node(self.root)
    def search(self,key):
        return search_bst(self.root,key)
    def searchValue(self,key):
        return search_value_bst(self.root,key)
    def findMax(self):
        return search_max_bst(self.root)
    def findmin(self):
        return search_min_bst(self.root)
    def insert(self, key, value=None):
        n = BSTNode(key,value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root,n)
    def delete(self, key):
        self.root = delete_bst(self.root,key)
    def display(self, msg='BSTMap'):
        def inorder(n):
            if n.left:
                inorder(n.left)
                print(n.key, end=' ')
            if n.right:
                inorder(n.right)  
                print(n.key, end=' ') 
        print(msg,end='')
        inorder(self.root)
        print()

map = BSTMap()
data = [35,18,7,26,12,3,68,22,30,99]

print("[삽입 연산] :",data)
for key in data:
    map.insert(key)
map.display("[중위 순회] : ")
if map.searchValue(26) != None : print("[탐식 26] : 성공")
else : print("[탐식 26] : 실패")
if map.search(25) != None : print("[탐식 25] : 성공")
else : print("[탐식 25] : 실패")

map.delete(3); map.display("[삭제 3] :")
map.delete(68); map.display("[삭제 68] :")
map.delete(18); map.display("[삭제 18] :")
map.delete(35); map.display("[삭제 35] :")