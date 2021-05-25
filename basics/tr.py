a=input('enter a number:')
b=input('enter another number:')

if a.isnumeric() and b.isnumeric():
    a=int(a)
    b=int(b)
    if a>b:
        print(a+b)
    else:
        print(a-b)
else:
    print('we need numbers not anything else:')



#for i in range(20):
    print(i)

#for x in range(10,20):
    print(x)

for y in range(10,20,3):
    print(y)