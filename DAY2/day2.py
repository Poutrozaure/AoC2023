
input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

colors = ["red","green","blue"]
red_max = 12
red_show =0
green_max = 13
green_show =0
blue_max=14
blue_show = 0
result = 0

#find max showned of each colors

#preprocess data
game_trial = ord(input[5])-48
test = input.split(";")
test[0]=test[0][7:]

for game,throw in enumerate(test):
        index = throw.find(colors[0])
        value = ord(throw[index-2])-48
        if index != -1 and value>red_show:
            red_show = throw[index-2]
            
        index = input.find(colors[1])
        value = ord(throw[index-2])-48
        if index != -1 and value>green_show:
            green_show = throw[index-2]
            
        index = input.find(colors[2])
        value = ord(throw[index-2])-48
        if index != -1 and value>blue_show:
            blue_show = throw[index-2]

print(red_show,green_show,blue_show)
#if(red_show<=red_max and green_show<= green_max and blue_show <= blue_max):
#    result +=1
