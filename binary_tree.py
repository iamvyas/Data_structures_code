#code under construction
class Node:
    def __init__(self, data):
        self.dataval = data
        self.nextval_left = None
        self.nextval_right = None

class linked_list:
    def __init__(self):
        self.root=None
        self.temproot = None

    #new node management
    def passon(self,temp):
        if(temp.dataval<self.temproot.dataval):
                if(self.temproot.nextval_left==None):
                    self.temproot.nextval_left=temp
                else:
                    self.temproot=self.temproot.nextval_left
                    self.passon(temp)
                return    
        if(temp.dataval>=self.temproot.dataval):
                if(self.temproot.nextval_right==None):
                    self.temproot.nextval_right=temp
                else:
                    self.temproot=self.temproot.nextval_right
                    self.passon(temp)
                return                       
        return    

    def new_node(self,no):
        temp = Node(no)
        if(self.root == None):
            self.root=temp
            return
        else:
            if(temp.dataval<self.root.dataval):
                if(self.root.nextval_left==None):
                    self.root.nextval_left=temp
                else:
                    self.temproot=self.root.nextval_left
                    self.passon(temp)
            if(temp.dataval>=self.root.dataval):
                if(self.root.nextval_right==None):
                    self.root.nextval_right=temp
                else:
                    self.temproot=self.root.nextval_right
                    self.passon(temp)        
            return    
    #new node managment    

    def print_root(self):
        print(self.root.dataval)
        return 

    #functions for print    

    def print_tree(self):
        self.printer(self.root)
        return

    def printer(self,troot):
        if(troot.dataval==None):
            return

        print(troot.dataval)    

        if(troot.nextval_left != None ):
            self.printer(troot.nextval_left)

        if(troot.nextval_right != None ):
            self.printer(troot.nextval_right)      
        return    
  
    #funtions for delete\
    def delete_tree(self,number):
        print("delete tree check")
        self.deleter(self.root,number)
        return

    def deleter(self,troot,number):
        print("deleter entry")
        x=int(troot.dataval)
        y=int(number)
        '''
        if(x==y):
            print("equality check")
            return
        elif(x!=y):
            print("inequality check")
            if(y<x):
                print("number is lesser than node")
            elif:
                print("number greater than node")    
        '''
        if(x==y):
            print("equality satisfied")
            if(troot.nextval_left!=None):
                print("left root aint empty")
                temp=troot.nextval_left
                troot.dataval=temp.dataval
                troot.nextval_left = self.deleter(temp,temp.dataval)
            elif(troot.nextval_right!=None):
                print("right root aint empty")
                temp=troot.nextval_right
                troot.dataval=temp.dataval
                troot.nextval_right = self.deleter(temp,temp.dataval)
            else:
                print("end of the tree reached")
                print(troot.dataval)
                troot = None
                return None

        if(x!=y):
            print("inequality satisfied")
            if(y<x and troot.nextval_left!= None):
                print("y<x condition passed")
                troot.nextval_left= self.deleter(troot.nextval_left,y)
            elif(y>x and troot.nextval_right != None):
                print("y>x condition passed")
                troot.nextval_right =self.deleter(troot.nextval_right,y)    
                               
        return troot
if __name__ == "__main__":
    linked = linked_list()
    choice=1
    while(choice!=4):
        if(choice==1):
            number = input("enter a number to add:")
            linked.new_node(number)
        if(choice==2):
            linked.print_tree()
            #print("under construction")
        if(choice==3):
            #linked.delete_node()
            linked.delete_tree(int(input("enter the number to be deleted:")))
        if(choice==5):
            linked.print_root()    
        print("1.add 2.print 3.delete 4.exit")
        choice=int(input("enter a choice:"))  #the int is used because the input takes the vlaue as a character which messes up with if condition            
