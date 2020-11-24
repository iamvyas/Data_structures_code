class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def new_node(self,no):
        temp = Node(no)
        if(self.head==None):
            self.head=temp
            self.tail=temp
            temp.nextval=None
            return
        temp.nextval=None
        self.tail.nextval=temp
        self.tail=temp
        return

    def printer(self):
        mapper=self.head
        while(mapper.nextval != None):
            print(" "+ mapper.dataval)
            mapper=mapper.nextval
        return        
if __name__ == "__main__":

    choice=0
    linked = linked_list()
    number = input("enter a number to add:")
    linked.new_node(number)

    while(choice != 3):
        print("1.add 2.print 3.quit")
        choice = input("enter a choice")
        if(choice==1):
            number = input("enter a number to add:")
            linked.new_node(number)
        elif(choice==2):
            linked.printer()
        elif(choice==3):
            print("thanks")
        else:
            print("invalid")           
''' '''



