a = input('enter something: ')

if a.isupper():
    print('a is upper')

if a.islower():
    print('a is lower')

if a.istitle():
    print('a is title case')

if a.isalpha():
    print('a only contains alphabet')

if a.isalnum():
    print('a contains alphabet and numbers')

if a.isnumeric():
    print('a only contains numbers')

if a.isspace():
    print('a only contains spaces')

if a.isprintable():
    print('a can be printed')

if a.isascii():
    print('is ascii character')

if a.isdigit():
    print('is contains digit only')

if a.isdecimal():
    print('is contains decimal only')

# check if input is float
b=input('enter a float')

if b.count('.') == 1 and b.replace('.','').isnumeric():
    print('b is float')
else:
    print('b is not a float')