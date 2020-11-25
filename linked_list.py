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
        
        print(" "+ mapper.dataval)

        return        
if __name__ == "__main__":
    linked = linked_list()
    choice=1
    while(choice!=3):
        if(choice==1):
            number = input("enter a number to add:")
            linked.new_node(number)
        if(choice==2):
            linked.printer()
        print("1.add 2.print 3.exit")
        choice=int(input("enter a choice:"))  #the int is used because the input takes the vlaue as a character which messes up with if condition            





