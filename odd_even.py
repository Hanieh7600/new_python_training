import random

print(random.randrange(1, 10))

list1=[]
evenlist=[]
oddlist=[]

size =  input('Enter size your arry:')

for i in range(int(size)):
    list1.append(int(input("item:")))

for i in range(len(list1)):
    if list1[i]% 2 != 0:
        oddlist.append(list1[i])

print(oddlist)

#---------

evenlist=[x for x in list1 if x %2 == 0  ]
print(evenlist)
