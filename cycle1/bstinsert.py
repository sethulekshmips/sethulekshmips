class node:
    def __init__(self,key):
        self.leftchild = None
        self.rightchild = None
        self.val = key

def insert(root,key):
    if root is None:
        return node(key)
    else:
        if(root.val==key):
            return root
        elif(root.val<key):
            root.rightchild=insert(root.rightchild,key)
        else:
            root.leftchild=insert(root.leftchild,key)
    return root
def inorder(root):
    if root:
        inorder(root.leftchild)
        print(root.val)
        inorder(root.rightchild)

r = node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
inorder(r)