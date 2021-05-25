print("Hello world")
a=2
b=5
c=a+b
print("add opt",c)
c=a%b
print("mod opt",c)
d=+45558
print(type(a),type(b),type(d))
e=-2.00265
print(type(e))

#bool
a = True
b = False
c = a and b
d = a or b
print(type(a),type(b),type(c),type(d))

#String -(str)

a='apple'
b="basket"
c='''hiiii how r u'''
print(type(a),type(b),type(c))


# Nonetype -None
a=None
b=None
print(type(a),type(b))


# data - structure

# list
a=[1,2,3,4,5,6]
print(type(a))

# tuple -> round brackets
a=(1,2,3,4,5,6,7)
b=1,23,4,6,6,6
print(type(a),type(b))

# set -> curly braces
a={1,3,3,3,5,66}
print(type(a))


# dict -> curly braces
d={"name":'apple','price':200}
c={1:1000,2:2000,3:3000}
print(type(c),type(d))

# programmatically check type ->
a=10
out=isinstance(a,int)
print("is an integer =>",out)
out=isinstance(a,float)
print("is an float =>",out)

price = input('enter the price of mouse you bought')
print(isinstance(price,int))
print(isinstance(price,float))
print(isinstance(price,str))



a=10
if a>5:
    print('this a is greater than 5')

if a== 10:
    print('this a is equal to 10')