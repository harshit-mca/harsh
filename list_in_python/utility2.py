#x=[23,2,13,12,43,56,12,97,98,25,15,3,43,343,2312]
#a =['alpha','beta','gamma']

#idx_of_876=x.index(876)
#print('876 occurs at index',idx_of_876)
x=[1,2,3,4,5,6,7,8,9]
y=[23,45,35,36,25,21,20]
z=[]
for i,j in zip(x,y):
    z.append(i+j)

print(x)
print(y)
print(z)

print(x+y)

x=[0,1]
size = int(input('enter size of series>>'))
for i in range(size):
    val=x[-1]+x[-2]
    x.append()