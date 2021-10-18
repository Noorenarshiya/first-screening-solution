integer_input = int(input('Enter number: '))

def odd_numbers(integer_input):
    mylist = []
    
    if integer_input % 2 == 0:
        integer_input -= 1
        
    for num in range(1,2*integer_input,2):
        mylist.append(num)
        
    return mylist

mylist = odd_numbers(integer_input)
print(','.join(str(o) for o in mylist))
