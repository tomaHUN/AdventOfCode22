import olvass
"""
try:
    with open('in.txt') as file
        print(file.read())    
except FileNotFoundError:  
    print("File not found")
"""

mano = olvass.olvass()
#print(mano)  
max = 0
now = 0
for i in mano:
    # print(now)

    if i != '': now += int(i)
    elif now > max : 
        max = now
        now = 0
    else : 
        now = 0
    
print(max)