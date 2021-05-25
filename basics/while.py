start=100
while start>=0:
    print(start)
    start -=5
print()

# sum of digit

number = 12346
total =0
while number>0:
    r = number % 10
    total +=r
    number=number//10

print('total',total)

while True:
    password = input('enter the secret password')
    if password == 'open seesame':
        print('welcome')
        break
else:
    print('haha')