
# Online Python - IDE, Editor, Compiler, Interpreter

with open('texte.txt') as f:
    inputs = f.readlines()
    
numbers = ["one","two","three","four","five","six","seven","eight","nine"]

final_number=0
for x,input in enumerate(inputs):
    indexes = []
    
    #indexes of numbers written
    for i in numbers:
        index_intermediate=[]
        index = 0
        while(index>=0 and index<len(input)):
                index = input.find(i,index)
                if(index>=0):
                    index_intermediate.append(index)
                    index+=1
                #else:
                    #index_intermediate.append()
        indexes.append(index_intermediate)
    
    print(indexes)
    
    #indexes of integer
    numbers_tab=[]
    coordinated_tab=[]
    for i,j in enumerate(input):
        number = ord(j)-48
        if(number>=0 and number<=9):
            numbers_tab.append(number)
            coordinated_tab.append(i)
    
    first_number_coord = 99999
    last_number_coord = 0
    first_number = 0
    last_number = 0
    
    
    print(coordinated_tab)
    
    for i,j in enumerate(coordinated_tab):
        #print(i)
        if j<=first_number_coord:
            first_number_coord = j
            first_number = numbers_tab[i]
        if j>=last_number_coord:
            last_number_coord = j
            last_number = numbers_tab[i]
    
    for i,j in enumerate(indexes):
        #print(j)
        if len(j)!= 0 and min(j)<=first_number_coord:
            first_number_coord = min(j)
            first_number = i+1
        if len(j)!= 0 and max(j)>=last_number_coord:
            last_number_coord = max(j)
            last_number = i+1
    
    print(x,first_number*10+last_number,input)
    final_number =final_number+(first_number*10+last_number)
    
print("final result",final_number)
