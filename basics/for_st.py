sentence = 'the theory of my life are not told by anyone'
print(len(sentence))

for char in sentence:
    print(char)

names = ['harshit','hrithk','allu arjun','katrina']

for name in names:
    print(name)

xset={1,2,3,4,5,4,6,4,8,7,8,2,32,2,4,10}
xtup=(1,2,2,2,2,2,2,3,3,2,24,6,4,64,6,46,4,64,64,8)
xdict={'a':'apple','b':'bsll'}

print('\ntuple')
for i in xset:
    print(i,end=' ')


print('\ndictionary')
for i in xtup:
    print(i,end=' ')

print('set')
for i in xdict:
    print(i,end=' ')



nums = [12,13,45,65,3,2,49,2,25,34,46,64,313,20]

for i,v in enumerate(nums):
    print(i,'-->',v)