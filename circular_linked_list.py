#working under the code
#this circular linked list works like a queue....most of its applications is used for queueing purpose so chill guys

class Node:
    def __init__(self, data):
        self.dataval = data
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
            temp.nextval=self.head
            return
        temp.nextval=self.head
        self.tail.nextval=temp
        self.tail=temp
        return    

    def delete_node(self):
        el_to_del = self.head
        self.head=self.head.nextval
        self.tail.nextval=self.head

        del el_to_del
        print("delete success")
        return
        

    def printer(self):
        mapper=self.head
        while(mapper.nextval != self.head):
            print(" "+ mapper.dataval)
            mapper=mapper.nextval
        
        print(" "+ mapper.dataval)

        return

    def print_headtail(self):
        print(self.head.dataval) 
        print(" ")
        print(self.tail.dataval)
        return            
if __name__ == "__main__":
    linked = linked_list()
    choice=1
    while(choice!=4):
        if(choice==1):
            number = input("enter a number to add:")
            linked.new_node(number)
        if(choice==2):
            linked.printer()
            print("test")
            linked.print_headtail()
        if(choice==3):
            linked.delete_node()    
        print("1.add 2.print 3.delete 4.exit")
        choice=int(input("enter a choice:"))  #the int is used because the input takes the vlaue as a character which messes up with if condition            





