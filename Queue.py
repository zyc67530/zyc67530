import sys
class Account:
    def __init__(self):
        self.id = '' #帳號
        self.password = '' #密碼
        self.web = '' #用以排序
        self.next = None

front = None
rear = None
ptr = None

def enqueue_f():
    global front
    global rear
    global ptr
    ptr = Account()

    ptr.id = input('Account id :')
    ptr.password = input('Account password ')
    ptr.web = input('Account website:')
    print()
    ptr.next = None
    if rear == None:
        front = ptr
    else:
        rear.next = ptr
    rear = ptr
    print()

def dequeue_f():
    global front
    global rear
    global ptr
    if front ==None:
        print('Queue is empty\n')
    else:
        del_data=front.data
        clear = front
        front=front.next
        clear=None
        print("%s has been deleted" % del_data)
    print()
def list_f():
    global front
    global rear
    global ptr
    count = 0
    if front ==None:
        print('Queue is empty\n')
    else:
        ptr=front
        while ptr != None:
            print('',end='')
            print(ptr.data)
            count+=1
            ptr = ptr.next
        print('total%d' %count)
    print()    
def main():
    option=0

    while True:
        print('1 Insert')
        print('2 Delete')
        print('3 List')
        print('4 Exit')
        try:
            option = eval(input('Choice:'))
        except ValueError:
            print('Not a number')
            print('Try again\n')
        
        if option == 1:
            enqueue_f()
        elif option == 2:
            dequeue_f()
        elif option ==3:
            list_f()
        elif option == 4:
            return 0
