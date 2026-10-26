# SID/Name :Rarindra Usaid Permana - 13226048
# Date : 30/09/2026
# Description : problem 3
lane=[0,0,0,0]
high=[]
highest=0

for i in range(4) :
    n = int(input("input number of vehicle in lane "+str(i+1)+" "))
    n= n*3+10
    lane[i]= n
    if(n>highest) :
        high.insert(0,i+1)
        highest=n
    else :
        high.insert(len(high),i+1)


for i in range(4) :
    print("the time length of lane "+str(i+1)+" is "+str(lane[i])+" seconds")
   
print("the priority lane will be lane "+str(high[0])+", then lane "+str(high[1])+", then lane "+str(high[2])+", and the last will be lane "+str(high[3]))

