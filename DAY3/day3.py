
with open('c:/AoC2023/DAY3/dataset.txt') as f:
    inputs=f.readlines()
    
coord_symb = []
##find the items coordinates
for x,my_input in enumerate(inputs):
    for y,char in enumerate(my_input):
        if(ord(char)<48 and ord(char)!=46): #case where we have a symbol
            coord_symb.append([x,y])
            
## check surroundings of symbol
for coord in coord_symb:
    x = coord[0]
    y = coord[1]
    
    #print(x,y)
    print("1")

print(coord_symb)
