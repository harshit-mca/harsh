numbers=[1,2,3,4,5,6,7,8,9]
names=['ravi','raju','harsh','anjali','prachi','obama','ritu']
heights=['ravi',6.5,'raju',4,'prachi',5.5]
info=[True,True,False,True,False]
marks_per_year=[[45,47,48],[46,43,42],[41,40,65]]
teams=[['rajy','rajeev']]

print(numbers,'size =',len(numbers))


# indexing
x=numbers[0]
print(x)
winner=names[3]
print(winner)
print(heights[-1])
print(heights[-2])

#slicing
first_two=numbers[:2]
last_two=numbers[-2:]
print(first_two)
print(last_two)


# for generation a large list
one_crore_items = list(range(1,10001))
even_list = list(range(2,201,2))
print(even_list)

x=[]
y=[1,2,3]

#adding single values to list
x.append(10)
x.append(20)
x.append(30)

y.append(4)
y.append(6)
y.append(8)

#insert single values to list
z=[1,3,4,5,6,7,5]
z.insert(1,2)


print(x)
print(y)
print(z)


# replace a value at an index

x[0]=100
x[-1]=500
z[3]=5
print(x)
print(y)
print(z)


# join a list to existing list
x.extend(22)
y.extend(x)
z.extend(y)

print(x)
print(y)
print(z)

print(numbers)
numbers.remove(4)
print(numbers)