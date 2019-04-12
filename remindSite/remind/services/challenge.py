from math import sqrt

PhysicsScoresX = [15,12,8,8,7,7,7,6,5,3]
HistoryScoresy = [10,25,17,11,13,17,20,13,9,15]
sumx =0
sumy =0
averagex=0
averagey=0
r = 0
uppery=0
upperx=0
lowerx=0
upper=0
lower=0




averagey = sum(HistoryScoresy)/len(HistoryScoresy)
averagex = sum(PhysicsScoresX)/len(PhysicsScoresX)


for i in range (0, len(PhysicsScoresX)):
    print(PhysicsScoresX[i])
    # upperx += (valuex - averagex) #ans += math.pow(z[i], k) * math.exp(math.pow(-z[i], 2) / 2)
    #print(upperx)
#print('UPPER X', upperx)

for j in range (0, len(HistoryScoresy)):
   print(HistoryScoresy[j])
   uppery += HistoryScoresy[j] - averagey


#print(uppery)

upper = upperx+uppery


lowerx = sqrt(pow(2,upperx))
lowery = sqrt(pow(2,uppery))
lower =lowerx*lowery

#print((upper/lower))
