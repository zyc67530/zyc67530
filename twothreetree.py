import sys
class Node:
    def __init__(self, key):
        self.key1 = key
        self.key2 = None
        self.left = None
        self.middle = None
        self.right = None
    def isLeaf(self):
        return self.left is None and self.middle is None and self.right is None
    def isFull(self):
        return self.key2 is not None
    def hasKey(self, key):
        if (self.key1 == key) or (self.key2 is not None and self.key2 == key):
            return True
        else:
            return False
    def getChild(self, key):
        if key < self.key1:
            return self.left
        elif self.key2 is None:
            return self.middle
        elif key < self.key2:
            return self.middle
        else:
            return self.right

root = None

def insert_f():
    global root
    key = int(input('enter key value:'))
    if root == None:
        root = Node(key)
    else:
        pKey, pRef = put_f(root, key)
        if pKey is not None:
            newnode = Node(pKey)
            newnode.left = root
            newnode.middle = pRef
            root = newnode

def put_f(node, key):
    if node.hasKey(key):
        return None, None
    elif node.isLeaf():
        return addtoNode(node, key, None)
    else:
        child = node.getChild(key)
        pKey, pRef = put_f(child, key)
        if pKey is None:
            return None, None
        else:
            return addtoNode(node, pKey, pRef)

def addtoNode(node, key, pRef):
    if node.isFull():
        return splitNode(node, key, pRef)
    else:
        if key < node.key1:
            node.key2 = node.key1
            node.key1 = key
            if pRef is not None:
                node.right = node.middle
                node.middle = pRef
        else:
            node.key2 = key
            if pRef is not None:
                node.right = pRef
        return None, None

def splitNode(node, key ,pRef):
    newnode = Node(None)
    if key < node.key1:
        pKey = node.key1
        node.key1 = key
        newnode.key1 = node.key2
        if pRef is not None:
            newnode.left = node.middle
            newnode.middle = node.right
            node.middle = pRef
    elif key < node.key2:
        pKey = key
        newnode.key1 = node.key2
        if pRef is not None:
            newnode.left = pRef
            newnode.middle = node.right
    else:
        pKey = node.key2
        newnode.key1 = key
        if pRef is not None:
            newnode.left = node.right
            newnode.middle = pRef
    node.key2 = None
    node.right = None
    return pKey, newnode

def display_f(node):
    print(node.key1, end='')
    if node.key2 != None:
        print(',', node.key2)
    else:
        print()
    if node.left != None:
        display_f(node.left)
    if node.middle != None:
        display_f(node.middle)
    if node.right != None:
        display_f(node.right)

def main():
    global root
    option = 0
    while True:
        print('***** Single list operation *****')
        print('1 insert node')
        print('2 delete node')
        print('3 display node')
        print('4 exit')
        print('******************')

        try:
            option = int(input('choice:'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        print()
        if option == 1: 
            insert_f()
        elif option == 2:
            pass
        elif option == 3:
            display_f(root)
        elif option == 4:
            return 0
        else:
            print('Wrong option')
    
