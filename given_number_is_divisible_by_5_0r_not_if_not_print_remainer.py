#---------method 1---------#
no = int(input("Enter a number : "))
if no % 5 == 0:
    print('Divisible')
else:
    if no < 0 :
        print(no % -5)
    else:
        print(no % 5)

#---------method 2---------#
'''
no = int(input("Enter a number : "))
if no % 5 == 0:
    print('Divisible')
else:
    if no < 0 :
        print('Not divisible and rem is : ',-no % 5)
    else:
        print('Not divisible and rem is : ',no % 5)
'''
