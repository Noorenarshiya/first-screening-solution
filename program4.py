list_1 = [1,2,8,9,12,46,76,82,15,20,30]
dictionary={} 
for i in range(1,10):
    dictionary[i] = 0
dictionary[1] = len(list_1)
for ele in list_1: 
    if ele % 2 == 0:
        dictionary[2] += 1
    if ele % 3 == 0:
        dictionary[3] += 1
    if ele % 4 == 0:
        dictionary[4] += 1
    if ele % 5 == 0:
        dictionary[5] += 1
    if ele % 6 == 0:
        dictionary[6] += 1
    if ele % 7 == 0:
        dictionary[7] += 1
    if ele % 8 == 0:
        dictionary[8] += 1
    if ele % 9 == 0:
        dictionary[9] += 1
        
        
print(dictionary)
