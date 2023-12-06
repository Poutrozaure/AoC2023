
with open('dataset.txt') as f:
    inputs=f.readlines()
    
#input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

colors = ["red","green","blue"]
red_max = 12
green_max = 13
blue_max=14
result = 0

for input in inputs:
    #print(input)
    red_show =0
    green_show =0
    blue_show = 0
    #find max showned of each colors
    
    #preprocess data
    test = input.split(";")
    index_1 = test[0].find(" ")
    index_2 = test[0].find(":")
    game_trial = int(input[index_1+1:index_2])
    test[0]=test[0][index_2+1:]
    print(test)
    for game,throw in enumerate(test):
            index = throw.find(colors[0])
            #print(index)
            if index!=-1 : 
                value = int(throw[index-3:index-1])
                if value>red_show:
                    red_show = value
                
            index = throw.find(colors[1])
            #print(index)
            if index!=-1 : 
                value = int(throw[index-3:index-1])
                if value>green_show:
                    green_show = value
                
            index = throw.find(colors[2])
            #print(index)
            if index!=-1 :
                value = int(throw[index-3:index-1])
                if value>blue_show:
                    blue_show = value
    
    
    print(red_show,green_show,blue_show)
    
    if(red_show<=red_max and green_show<= green_max and blue_show <= blue_max):
        result +=game_trial
        
print(result)
