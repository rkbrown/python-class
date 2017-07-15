print('***********************************************************************')
print('**************************** CODE STRUCTURES **************************')
print('***********************************************************************')
print('')
print('-- loops --')

print('(example 1) -------------------------------------------------------------------')

counter = 0
while counter <= 20:
    print('number ', counter)
    counter = counter + 1

print('(example 2) -------------------------------------------------------------------')

count = 1
while count <= 10:
    if (count == 2):
        print('***')
    else:
        print('hey ' , count , 'ho')
        
    count += 1

print('(1) -------------------------------------------------------------------')
# make a "while" loop
MW = 1000
while MW <= 1030:
    if (MW == 1002):
        print('Welcome')
    elif (MW == 1016):
        print ('Student' , MW , 'We do not accept Matthews ')
        
    else:
        print('Welcome Student ' , MW)
    MW += 2

print('')
print('')
print('(2) -------------------------------------------------------------------')
# make another "while" loop


print('')
print('')
print('(3) -------------------------------------------------------------------')
# make a while loop that prints only even numbers, but your counter can only go up by ones!!!!
pieman = 56
while pieman <= 164:
    if (pieman % 2 == 0):
        print(pieman)
    else:
        print('modulo = ', pieman % 2)
        
    
    pieman += 1
    

print('')
print('')
print('(4) -------------------------------------------------------------------')
