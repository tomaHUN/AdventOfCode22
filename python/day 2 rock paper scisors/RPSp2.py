
import olvass


RPSbe = olvass.olvass()
#print(ord("A"))

#RPSbe[adott kör][0= ellenfél(abc) 2=lose draw win(xyz)]
# x = 0p   y = 3p  z=6p
# x = 88      !!! (x-88)*3 = win points
# 65 = A 
# enemA(winX/myplay)
# A  rock(lose/scisor)= 3 point ;rock(draw)= 1 point ;rock(win/paper) = 2       
# B  paper(lose/rock)= 1 point ;paper(draw)= 2 point ;paper(win/scisor) = 3
# C  scisor(lose/paper)= 2 point ;scisor(draw)= 3 point ;scisor(win/rock) = 1

# lose = -1 pont with overflow   win +1 pont with overflow
# overflow = if 0 =3        if 4 = 1




points = 0
for i in RPSbe:
    #print(points)
    #print(i)
    # geting 0, 1, 2 for lose draw win
    winor = (ord(i[2]) - 88)
    # adding points for win
    points +=  winor * 3
    #print(points)
    RPSenemy = ord(i[0]) - 64
    #print(winor ,   RPSenemy)  
    if winor == 1 : points+= RPSenemy  # if draw we just get the points
    elif winor == 0 : points += ((RPSenemy + 1)% 3)+1 # we need to -1 but to make with %3 we can only get 0,1,2 so -2 and at the and +1 to get to 1,2,3
    elif winor == 2 : points += ((RPSenemy + 3)% 3)+1  # +1
    
print("vege",points)