l=[]
ll=[]
for i in range(6):
    ll.append(input())
for i in ll:
    if(i=="G" or i=="g"):
        l.append(0)
    else:
        l.append(int(i))
print("enter your floor number")
a=int(input())
aa=[]
for i in range(6):
    aa.append(abs(l[i]-a))
near=aa[0]
le=1
for i in range(1,6):
    if(aa[i]<near):
        le+=1
        break
    else:
        le+=1
print("Nearet lift number: ",le)
