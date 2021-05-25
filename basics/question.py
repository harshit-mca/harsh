# numbers which are divisible by 7 and multiple of 5 between 1500 and 2700(both included)
# count a number of even and odd numbers from a series of numbers.
# program to ger the fabonacci series between 0 to 50.
# program that accepts a word from the user and reverse it.

for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i)


# =>2

n=int(input('enter the number: '))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print('all odds',odd)
print('all evens',even)

# =>3

a=0
b=1
print(a,b,end=' ')
for i in range(50):
    c=a+b
    if c>50:
        break
    print(c,end=' ')
    a=b
    b=c
print('\n')

# =>4        

word=input('enter your word : ')

if len(word)>0:
    print(word,len(word))

for i in range(len(word)-1,0,-1):
    print(word[i],end='')


