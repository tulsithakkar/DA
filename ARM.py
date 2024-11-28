#ARM algoritm

#tran=[]
#temp=[]
#ni = int(input("how many transactionyou want: "))
#for i in range(ni):
#    nj = int(input("number of items transactionyou want: "))
#    for j in range(nj):
#        k = input("enter item: ")
#        temp.append(k)
#    tran.append(temp)
#    temp=[]
tran=[['a','b','c'],['a','d'],['c','e','f']]
print(tran)

#c1 list
c1=[]
for i in tran:
    for j in i:
        if j not in c1:
            c1.append(j)
print(c1)

#c1 count
cnt =0
for i in c1:
    for j in tran:
        for k in j:
            if(k==i):
                cnt+=1
    print(f"{i}:{cnt}")
    cnt =0

#c2 list
c2=[]
temp=[]
i=0
l = len(c1)
for i in range(l):
    j =i+1
    for p in range(j,l):
        if p not in c2:
            temp.append(c1[i])
            temp.append(c1[j])
            c2.append(temp)
            temp=[]
            j+=1
    i+=1
print(c2)

#c2 count

countitem2=[]
for i in c2:
    count2=0
    for j in tran:
        flag =True
        for p in i:
            if p not in j:
                flag = False
                break
        if flag:
            count2+=1
    print(f"{i}: {count2}")

#c3 list
c3=[]
for i in range(len(c1)):
    for j in range(i+1,len(c1)):
        for k in range(j+1,len(c1)):
            c3.append([c1[i],c1[j],c1[k]])
print(c3)

#count c3
countitem3=[]
for i in c3:
    count3=0
    for j in tran:
        flag = True
        for p in i:
            if p not in j:
                flag = False
                break
        if flag:
            count3+=1
    print(f"{i}:{count3}")

























            

        
            



































    












        
