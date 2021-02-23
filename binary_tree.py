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

    def delete_node(self,index):
        el_to_del = self.root
        if(el_to_del.dataval==index):
            print("delete the part and join with next highest number")
            el_to_del.dataval=self.replacer(el_to_del)

        else:
            if(el_to_del.nextval_right!=None):
                el_to_del.dataval= self.rec_delete(el_to_del.nextval_right,index)
            else:
                el_to_del.dataval= self.rec_delete(el_to_del.nextval_left,index)     

        print("delete success")
        return

    def rec_delete(self,del_node,index):
        el_to_del = del_node
        if(el_to_del.dataval==index):
            el_to_del=self.replacer(el_to_del)

        else:
            if(el_to_del.nextval_right!=None):
                el_to_del.dataval= self.rec_delete(el_to_del.nextval_right,index)
            else:
                el_to_del.dataval= self.rec_delete(el_to_del.nextval_left,index)

        return  el_to_del.dataval   
        

    def print_root(self):
        print(self.root.dataval)
        return  

    def printer(self):
        mapper=self.root
        if(mapper.nextval_left != None ):
            temp_number=mapper.nextval_left
            self.printrec(mapper.nextval_left)
            print(temp_number.dataval)

        if(mapper.nextval_right != None ):
            temp_number=mapper.nextval_right
            self.printrec(mapper.nextval_right)
            print(temp_number.dataval)

        print(mapper.dataval)      


        return

    def printrec(self,pointed_node):
        nxt_node = pointed_node
        if(nxt_node.nextval_left != None ):
            temp_number=nxt_node.nextval_left
            self.printrec(nxt_node.nextval_left)
            print(temp_number.dataval)

        if(nxt_node.nextval_right != None ):
            temp_number=nxt_node.nextval_right
            self.printrec(nxt_node.nextval_right)
            print(temp_number.dataval)

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
            #print("under construction")
        if(choice==3):
            #linked.delete_node()
            print("under construction")  
            linked.print_root()  
        print("1.add 2.print 3.delete 4.exit")
        choice=int(input("enter a choice:"))  #the int is used because the input takes the vlaue as a character which messes up with if condition            
