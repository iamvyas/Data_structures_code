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

    def delete_node(self,index):
        temp=self.head
        i=0
        invalid_flag=0
        #locate the node
        if(int(index) == 1):
            self.head=temp.nextval
            del temp
            print("delete succcess" + self.head.dataval)
            return
        while(i!=int(index)-2):
            temp=temp.nextval
            if(temp.nextval == None):
                invalid_flag=1
                break
            else:
                i +=1
        if (invalid_flag==1):
            print("position out of range")
            return
        bag=temp.nextval
        temp.nextval=bag.nextval
        del bag
        print("delete succcess")    
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
    while(choice!=4):
        if(choice==1):
            number = input("enter a number to add:")
            linked.new_node(number)
        if(choice==2):
            linked.printer()
        if(choice==3):
            number = input("enter position to be deleted:")
            linked.delete_node(number)    
        print("1.add 2.print 3.delete 4.exit")
        choice=int(input("enter a choice:"))  #the int is used because the input takes the vlaue as a character which messes up with if condition            





