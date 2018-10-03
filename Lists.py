spam = [[10, 5, 7, 56], ['dog', 'cat', 'bird', 'bat']]
print(spam)

del spam[0][0]
print(spam)

print('dog' in spam[1])

print('doug' not in spam)

supplies = ['pens', 'erasers', 'flame-throwers', 'clips']
for i in range(len(supplies)):
    print('index ' + str(i) + ' in supplies is: ' + str(supplies[i]))

item1, item2, item3, item4 = supplies
print(item1)
print(item2)
print(item3)
print(item4)

supplies.sort()
print(supplies)

spam[0].sort()
spam[1].sort()
print(spam)
