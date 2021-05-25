# number which is divided by itself.

num = int(input('enter a number : '))

# for-else => we can use it to find if our loop has completed all iterations successfully.
for i in range(2,num):
    print(num,'%',i,'=',num % i)
    if num % i ==0:
        print('non prime')
        break
else:
    print('prime')



#aggregator 
#wap to find the sum of all odd and even numbers in a range given by users.

end = 10

# normal code
oddtotal = 0
eventotal = 0
for i in range(end+1):
    if i%2 == 0:
        eventotal += i   # eventotal = eventotal+1
    else:
        oddtotal += i

print('sum of all odds',oddtotal)
print('sum of all even',eventotal)

#pythonic

print('sum of all evens',sum(range(0,end+1,2)))
print('sum of all odds',sum(range(1,end+1,2)))

#vowels 
message = 'this is an example message'

for char in message:
    if char in 'aeiou':
        print(char)


# to display mean,max,min,sum

data = [2,3,2,5,0,5656,2,65,2,36,25,26,14,25,236,356,512,298,78,9]


    