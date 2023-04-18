import olvass


RPSbe = olvass.olvass()

#print(ord(RPSbe[1][2]))

#RPSbe[adott kör][0= ellenfél(abc) 2=saját(xyz)]
# a/x = rock  , b/y = paper c/z = scisor
# ord = ascii number , chr = back to char
# x-a = 23 ... 21     (sorban vannak) z-a = 25
# 88 =x so my number -87 = points i get

# 23 = draw     (3p)
# 22,25 = lose  (0p)
# 21,24 = win   (6p)

#print(ord(RPSbe[0][2])-ord(RPSbe[0][0]))
#print(ord("z")-ord("c"))

points = 0
for i in RPSbe:
    #print(points)
    # adding point for my choice
    points +=  int(ord(i[2])) - 87
    #print(points)
    winornot = ord(i[2]) - ord(i[0])
    if winornot == 23: points += 3
    elif winornot == 21 : points += 6
    elif winornot == 24 : points += 6
    
    
print("vege",points)        