
class Account:
    def __init__(self):
        self.id = '' #帳號
        self.password = '' #密碼
        self.web = '' #用以排序
        self.next = None

ptr = None
current = None
prev = None

head = Account()
head.next = None


def insert_f():
    global ptr
    global head
    global current
    global prev

    ptr = Account()
    ptr.next = None
    ptr.id = input('Account id :')
    ptr.password = input('Account password ')
    ptr.web = input('Account website:')
    print()
    
    prev = head
    current = head.next
    ptr.next = current
    prev.next = ptr

def delete_f():
    global head
    global current
    global prev

    del_web = ''
    if head.next == None:
        print('No Account record\n')
    else:
        del_web = input('Delete Account web:')
        prev = head
        current = head.next
        while current != None and del_web != current.web:
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next
            current = None
            print('\n Account web: %s already deleted\n' % del_web)
        else:
            print('\n Account web: %s not found\n' % del_web)

def modify_f():
    global head
    global current
    global prev
    global ptr

    if head.next == None:
        print('No Account record\n')
    else:
        modify_web = input('Modify Account web: ')
        prev = head
        current = head.next
        while current != None and modify_web != current.web:
            prev = current
            current = current.next
        if current != None :
            print('\n Account web :%s' % current.web)
            print('  Account id: %s\n' % current.id)
            print('  Account password: %s\n' % current.password)
            prev.next = current.next
            current = None
            newid = input('please enter new id:')
            newpassword = input('please enter new password:')
            ptr = Account()
            ptr.next = None
            ptr.web = modify_web
            ptr.id = newid
            ptr.password = newpassword
            prev = head
            current = head.next

            ptr.next = current
            prev.next = ptr
            print(' Account updated successfully!\n')
        else:
            print('\n Account %s not found!\n' % modify_web)

def display_f():
    global head
    global current
    count = 0
    if head.next == None:
        print('No Account record\n')
    else:
        current = head.next
        while current != None :
            print('web:%s' % current.web)
            print('id:%s' % current.id)
            print('password:%s' % current.password)
            print('--------------------------------')
            count += 1
            current = current.next
        print('total: %d'%count)

def search_f():
    global head
    global current
    search_web = input('search web:')
    if head.next == None:
        print('No Account record\n')
    else:
        current = head.next
        while current != None and search_web != current.web:
            current = current.next
        if current != None :
            print('web:%s' % current.web)
            print('id:%s' % current.id)
            print('password:%s' % current.password)
        else:
            print('\n Account %s not found!\n' % search_web)
    
    
def main():
    option = 0
    while True:
        print('***** Single list operation *****')
        print('1 insert')
        print('2 delete')
        print('3 modify')
        print('4 display')
        print('5 search')
        print('6 exit')
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
            delete_f()
        elif option == 3:
            modify_f()
        elif option == 4:
            display_f()
        elif option == 5:
            search_f()
        elif option == 6:
            return 0
