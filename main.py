import sys
import LinkedList
import Queue
import Stackfunction
import BST
import AVLtree
import Heap
import twothreetree

if __name__ == "__main__":#主程式的主程式
    option = 0
    while True:
        print('***** Please choose a data structure Operation *****')
        print('1. Linked List')
        print('2. Queue')
        print('3. Stack')
        print('4. Binary Search Tree')
        print('5. AVL tree')
        print('6. Heap')
        print('7. 2-3 tree')
        print('8. exit')
        print('****************************************************')

        try:
            option = int(input('choice:'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        print()
        if option == 1: 
            LinkedList.main()
        elif option == 2:
            Queue.main()
        elif option == 3:
            Stackfunction.main()
        elif option == 4:
            BST.main()
        elif option == 5:
            AVLtree.main()
        elif option == 6:
            Heap.main()
        elif option == 7:
            twothreetree.main()
        elif option == 8:
            sys.exit(0)
        else:
            print('Wrong option')
    
    