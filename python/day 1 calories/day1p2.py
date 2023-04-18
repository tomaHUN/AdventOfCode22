import olvass

mano = olvass.olvass()


max = [0,0,0]
now = 0
for i in mano:
    # print(now)
    # adding up calories until next elfe 
    if i != '': now += int(i)
    # finding out if it's in 3 bigest
    elif now > min(max) : 
        # findig the index of the smallest element
        min_value = min(max)
        min_index = max.index(min_value)
        #replacing the smallest of the 3 with the new value
        max[min_index] = now
        now = 0
    else : 
        now = 0
        

print(max) 
       
print(sum(max))       