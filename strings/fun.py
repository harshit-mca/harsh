#msg = "apple,banana,cucumber,kiwi,cheeku"
#words = msg.rsplit(',',2)
#print(words)

#msg1 = 'hello the sun rises in the east and sets in the west.'
#msg=msg1.split('in')
#print(msg)

mg="hello how are you nd how old are you."
v=['a','e','i','o','u']
for i in mg:
    if i not in v:
        mg=mg.replace(i,'')
print(mg)


mg="hello how are you nd how old are you."
v=['a','e','i','o','u']
l=0
for i in mg:
    if i in v:
        l+=1
print(l)


