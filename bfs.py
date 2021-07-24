graph=[[1,2],[3],[],[4,5],[1,2,5],[]]
lst=[0,0,0,0,0,0]
stak=[]
lst[0]=1
ans=[]
stak.append(0)
while(stak!=[]):
    num=stak.pop(0)
    ans.append(num)
    for i in graph[num]:
        if(lst[i]==0):
            stak.append(i)
            lst[i]=1
    
print(ans)

#[0, 1, 2, 3, 4, 5]
