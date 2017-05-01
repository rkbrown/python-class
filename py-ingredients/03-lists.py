print('***********************************************************************')
print('******************************** LISTS ******************************')
print('***********************************************************************')
print('')
print('')
print('(1) -------------------------------------------------------------------')
print('')
print('')
# a LIST is a list of things
# HINT: make a list of things like this:
# friends = ['Gavin', 'Aidan', 'Jacob']
# create the friends list above ( ^ ) and print it out
# friends
friends = ['Gavin', 'Aidan', 'Jacob']
print(friends)
print('')
print('')
print('(2) -------------------------------------------------------------------')
print('')
print('')
# print out the first friend on the list
# HINT: get a list item by specifying its OFFSET (its place number) EX: alphabet[18]
print(friends[0])

print('')
print('')
print('(3) -------------------------------------------------------------------')
print('')
print('')
# print out the second friend on the list
print(friends[1])

print('')
print('')
print('(4) -------------------------------------------------------------------')
print('')
print('')
# add a new friend to this friend list and print out the new list
# HINT: add items to list with .append([thing you want to add]). EX: alphabet.append('z')
friends.append('Bobby Joe Jr.')

print('')
print('')
print('(5) -------------------------------------------------------------------')
print('')
print('')
# change the new friend's name to 'Bob' print out the new list
# HINT: your can change a list item by specifying its OFFSET and using the = sign to assign a new name

friends[3] = 'Bob'
print(friends)
print('')
print('')
print('(6) -------------------------------------------------------------------')
print('')
print('')
# create a new list of kid's names and then add those kids to the friends list
# print out the new list
# HINT: you can combine two lists with .extend() EX: alphabet.extend(newStuff)
# or, you can combine two lists with += EX: alphabet += newStuff
Peeps = ['pepe','Dora','LLAMA MAMA','Tiny Chocolate Dufas']
print(Peeps)
friends.extend(Peeps)
print(friends)
print('')
print('')
print('(7) -------------------------------------------------------------------')
print('')
print('')
# find out how many friends are on the list now, print it out
# HINT: you can count items on a list by measuring its length using len() EX: alphabetNumber =len(alphabet)
print(len(friends))


print('')
print('')
print('(8) -------------------------------------------------------------------')
print('')
print('')
# Remember STRINGS? Remember you alphabet string from last lesson?
# 1) re-create your alphabet STRING
# 2) convert it to a LIST 
# HINT: you can convert a string to a list with list() EX: catList = list('cat') creates ['c','a','t']
# 3) print out the letter k
# 4) print out the letter z
# HINT: use negative OFFSET numbers to count backwards from the end of a list EX: catList[-1] = 't'
# 5) using a negative offset number, print out the letter b

alphabetlist = list('abcdefghijklmnopqrstuvwxyz')
print (alphabetlist)
print (alphabetlist[10])
print (alphabetlist[-1])
print (len(alphabetlist))
print (alphabetlist[-25])