
import sys

class Student:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.score = 0
        self.bf = 0
        self.llink = None
        self.rlink = None

root = None
ptr = None
current = None
prev = None
pivot = None
pivot_prev = None
nodecount = 0

def type_ll():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.llink
    temp = pivot_next.rlink

    pivot_next.rlink = pivot
    pivot.llink = temp

    if pivot == root:
        root = pivot_next
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = pivot_next
    else:
        pivot_prev.rlink = pivot_next

def type_rr():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.rlink
    temp = pivot_next.llink

    pivot_next.llink = pivot
    pivot.rlink = temp

    if pivot == root:
        root = pivot_next
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = pivot_next
    else:
        pivot_prev.rlink = pivot_next   

def type_lr():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.llink
    temp = pivot_next.rlink

    pivot.llink = temp.rlink
    pivot_next.rlink = temp.llink
    
    temp.llink = pivot_next
    temp.rlink = pivot


    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp

def type_rl():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.rlink
    temp = pivot_next.llink

    pivot.rlink = temp.llink
    pivot_next.llink = temp.rlink
    
    temp.rlink = pivot_next
    temp.llink = pivot


    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp

def insert_f():
    global nodecount

    print('\n insert node')
    id_t = eval(input('student id:'))
    name_t = input('student name:')
    score_t = eval(input('student score:'))

    print('\n new node')
    print('id: %d  name: %s score: %d'%(id_t, name_t, score_t))

    nodecount += 1

    sort_f(id_t, name_t, score_t)

def sort_f(id_t, name_t, score_t):
    global ptr
    global root
    global current
    global prev
    global pivot

    op = 0
    current = root

    while current != None and id_t != current.id:
        if id_t < current.id:
            prev = current
            current = current.llink
        else:
            prev = current
            current = current.rlink
    
    if current == None or id_t != current.id:
        ptr = Student()
        ptr.id = id_t
        ptr.name = name_t
        ptr.score = score_t
        ptr.llink = None
        ptr.rlink = None
        if root == None:
            root = ptr
        elif ptr.id < prev.id:
            prev.llink = ptr
        else:
            prev.rlink = ptr
        bf_count(root)
        pivot = pivot_find()
        if pivot != None:
            op = type_find()
            if op == 11:
                type_ll()
            elif op == 22:
                type_rr()
            elif op == 12:
                type_lr()
            elif op == 21:
                type_rl()
        bf_count(root)
    else:
        print('add new node error')
        print('student <%s> has existed!'%(id_t))

def bf_count(trees):
    if trees != None:
        bf_count(trees.llink)
        bf_count(trees.rlink)

        trees.bf = height_count(trees.llink) - height_count(trees.rlink)

def height_count(trees):
    if trees == None:
        return 0
    elif trees.llink == None and trees.rlink == None:
        return 1
    elif height_count(trees.llink) > height_count(trees.rlink):
        return 1 + height_count(trees.llink)
    else:
        return 1 + height_count(trees.rlink)
    
def pivot_find():
    global root
    global current
    global prev
    global pivot
    global pivot_prev
    global nodecount

    current = root
    pivot = None

    for i in range(nodecount):
        if current.bf < -1 or current.bf > 1:
            pivot = current
            if pivot != root:
                pivot_prev = prev
            print('current pivot id: ',current.id)
        if current.bf > 0:
            prev = current
            current = current.llink
        elif current.bf < 0:
            prev = current
            current = current.rlink
    
    return pivot

def type_find():
    global current
    global pivot

    op_r = 0
    current = pivot
    for i in range(2):
        if current.bf > 0:
            current = current.llink
            if op_r == 0:
                op_r += 10
            else:
                op_r += 1
        elif current.bf <0:
            current = current.rlink
            if op_r == 0:
                op_r += 20
            else:
                op_r += 2

    return op_r


def list_f():
    global root

    if root == None:
        print('\n No student record exist!')
    else:
        list_data()

def list_data():
    global root

    print('\n list data')
    print('%-10s %-15s %-5s'%("id", "name", "score"))
    inorder(root)

def inorder(trees):
    try:
        inorder(trees.llink)
        print('%-10s %-15s %-5s'%(trees.id , trees.name, trees.score))
        inorder(trees.rlink)
    except BaseException:
        None


def delete_f():
    global root
    global current
    global prev
    global pivot
    global nodecount

    clear = None
    if root == None:
        print('\n no student record exist!')
    else:
        print('\n delete node')
        id_t = eval(input('enter student id:'))
        tempn = id_t
        current = root

        while current != None and id_t != current.id:
            if id_t < current.id:
                prev = current
                current = current.llink
            else:
                prev = current
                current = current.rlink
        
        if current != None and id_t == current.id:
            if current.llink == None and current.rlink == None:
                clear = current
                if id_t == root.id:
                    root = None
                else:
                    if id_t < prev.id:
                        prev.llink = None
                    else:
                        prev.rlink = None
                clear = None
            else:
                if current.llink != None:
                    clear = current.llink
                    while clear.rlink != None:
                        prev = clear
                        clear = clear.rlink
                    current.id = clear.id
                    current.score = clear.score
                    if current.llink == clear:
                        current.llink = clear.llink
                    else:
                        prev.rlink = clear.rlink
                else:
                    clear = current.rlink
                    while clear.llink != None:
                        prev = clear
                        clear = clear.llink
                    current.id = clear.id
                    current.score = clear.score
                    if current.rlink == clear:
                        current.rlink = clear.rlink
                    else:
                        prev.llink = clear.rlink
                clear = None
            
            bf_count(root)
            if root != None:
                pivot = pivot_find()
                while pivot != None:
                    op = type_find()
                    if op == 11:
                        type_ll()
                    elif op == 22:
                        type_rr()
                    elif op == 12:
                        type_lr()
                    elif op == 21:
                        type_rl()
                    bf_count(root)
                    pivot = pivot_find()
            
            nodecount -= 1
            print('\n student %s has been deleted' % tempn)
        else:
            print('\n student %s not found!' % tempn)

def modify_f():
    global root
    global current

    if root == None:
        print('\n no student record exist')
    else:
        print('\n modify node')
        id_t = eval(input('student id:'))

        current = root
        while current != None and id_t != current.id:
            if id_t < current.id:
                current = current.llink
            else:
                current = current.rlink
        

        if current != None:
            print('\n student id:', current.id)
            print('\n student name:', current.name)
            print('\n student score:', current.score)
            print('\n')
            current.score = eval(input('enter new score:'))
            print('data updated successfully')
        else:
            print('\n student :', id_t, 'not found!!')
    print()


def main():
    option = 0
    while True:
        print('***** Single list operation *****')
        print('1 insert node')
        print('2 delete node')
        print('3 modify node')
        print('4 display node')
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
            list_f()
        elif option ==5:
            return 0
        else:
            print('Wrong option')
    