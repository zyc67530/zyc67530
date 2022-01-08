import sys

class Student:
    name = ''
    score = 0
    llink = None
    rlink = None

root = None

def show_f():
    global root
    if root == None:
        print('No student record!')
        return
    print('\nshow data in inorder')
    inorder(root)
    print('\nshow data in preorder')
    preorder(root)
    print('\nshow data in postorder')
    postorder(root)

def preorder(node):
    if node != None:
        print('%-15s %-3d' % (node.name, node.score))
        preorder(node.llink)
        preorder(node.rlink)
 

def postorder(node):
    if node != None:
        postorder(node.llink)
        postorder(node.rlink)
        print('%-15s %-3d' % (node.name, node.score))


def inorder(node):
    if (node != None):
        inorder(node.llink)
        print('%-15s %-3d' % (node.name, node.score))
        inorder(node.rlink)

def insert_f():
    name = ''
    score = 0
    print('\ninsert data')
    name = input('enter a student name')
    score = eval(input('enter a score'))

    access(name,score)

def search(target):
    global root
    node = root
    while node != None:
        if target == node.name:
            return node
        elif target < node.name:
            node = node.llink
        else:
            node = node.rlink
    
    return node



def access(name, score):
    global root
    node = None
    prev = None
    if search(name) != None:
        print('student %s has existed!' % name)
        return
    ptr = Student()
    ptr.name = name
    ptr.score = score
    ptr.rlink = None
    ptr.llink = None
    if root == None:
        root = ptr
    else:
        node = root
        while node != None:
            prev = node
            if ptr.name < node.name:
                node = node.llink
            else:
                node = node.rlink
        if ptr.name < prev.name:
            prev.llink = ptr
        else:
            prev.rlink = ptr

def delete_f():
    global root
    name = ''
    if root == None:
        print('No student record')
        return
    print('\ndelete data')
    name = input('enter student name')

    removing(name)

def removing(name):
    global root
    del_node = search(name)
    if del_node == None:
        print('student %s not found!' % name)
        return

    if del_node.llink != None or del_node.rlink != None:
        del_node = replace(del_node)
    else:
        if del_node == root:
            root = None
        else:
            connect(del_node,'n')
    del_node = None
    print('student %s has been deleted!' % name)

def connect(node, link):
    parent = search_p(node)
    if node.name <parent.name:
        if link == 'r':
            parent.llink = node.rlink
        elif link == 'l':
            parent.llink = node.link
        else:
            parent.llink = None
    elif link == 'r':
        parent.rlink = node.rlink
    elif link =='l':
        parent.rlink = node.llink
    else:
        parent.rlink = None

def search_p(node):
    global root
    parent = root
    while parent != None:
        if node.name < parent.name:
            if node.name == parent.llink.name:
                return parent
            else:
                parent = parent.llink
        elif node.name == parent.rlink.name:
            return parent
        else:
            parent = parent.rlink
    return None

def replace(node):
    re_node = None
    re_node = search_re_r(node.rlink)
    if re_node == None:
        re_node = search_re_l(node.llink)
    if re_node.rlink != None:
        connect(re_node, 'r')
    elif re_node.llink != None:
        connect(re_node, 'l')
    else:
        connect(re_node, 'n')
    node.name = re_node.name
    node.score = re_node.score
    return re_node

def search_re_l(node):
    re_node = node
    while re_node != None and re_node.rlink != None:
        re_node = re_node.rlink
    return re_node

def search_re_r(node):
    re_node = node
    while re_node != None and re_node.llink != None:
        re_node = re_node.llink
    return re_node

def modify_f():
    global root
    node = None
    name = ''
    if root == None:
        print('No student record!')
        return
    else:
        print('\n modify datd')
        name = input('enter a student name')

        node = search(name)
        if node == None:
            print('student %s not found' % name)
        else:
            print('original name',node.name)
            print('original score',node.score)
            node.score = eval(input('enter new score:'))
            print('Student %s has been modified' % name)


def main():
    option = 0
    while True:
        print('***** Single list operation *****')
        print('1 insert')
        print('2 delete')
        print('3 modify')
        print('4 display')
        print('5 exit')
        print('******************')

        try:
            option = int(input('choice:'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        print()
        if option == 1: 
            insert_f()
        elif option ==2:
            delete_f()
        elif option ==3:
            modify_f()
        elif option ==4:
            show_f()
        elif option ==5:
            return 0
        else:
            print('Wrong option')
