
class Account:
    def __init__(self):
        self.id = '' #帳號
        self.password = '' #密碼
        self.web = '' #用以排序

MAX = 20
st = [''] * MAX
top = -1
ptr = None

def push_f():
    global MAX
    global st
    global top
    global ptr

    if top >= MAX-1:
        print('stack is full')
    else:
        ptr = Account()
        ptr.id = input('Account id :')
        ptr.password = input('Account password ')
        ptr.web = input('Account website:')
        print()
        top += 1
        st[top] = ptr
    print()

def pop_f():
    global st
    global top
    if top<0:
        print('stack is empty')
    else:
        i = st[top]
        print('\n %s account has been deleted' % i.web)
        top -= 1
    print()

def list_f():
    global st
    global top
    current = None
    if top<0:
        print('Stack is empty')
    else:
        i = top
        while i >= 0:
            current = st[i]
            print('web:%s' % current.web)
            print('id:%s' % current.id)
            print('password:%s' % current.password)
            print('--------------------------------')
            i -= 1
    print() 

def search_f():#應用pop
    global st
    global top
    temp = [] * MAX
    current = None
    temp = st
    temptop = top
    search_web = input('search web:')
    if top < 0:
        print('stack is empty')
    else:
        current = temp[temptop]
        while current.web != search_web and temptop>=0:
            current = temp[temptop]
            temp.pop()
            temptop -= 1
            if current.web == search_web:
                print('web:%s' % current.web)
                print('id:%s' % current.id)
                print('password:%s' % current.password)
                break
        if temptop < 0:
            print('Account not found!')
    print() 

def main():
    option = 0
    while True:
        print('1.insert')
        print('2.delete')
        print('3.list')
        print('4.search')
        print('5.exit')
        try:
            option = eval(input('Please choose an opreation'))
        except ValueError:
            print('Not a number')
            print('try again')
        if option == 1:
            push_f()
        elif option == 2:
            pop_f()
        elif option == 3:
            list_f()
        elif option == 4:
            search_f()
        elif option == 5:
            return 0
        else:
            print("Not a correct number")
            return

