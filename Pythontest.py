# taking the file 

f = open("./input.txt", 'r')
#into lsit of lines 
lines = f.readlines()
#go through those lines and check if better than current best
best = 0
cur = 0
for x in lines:
    #print(x)
    #checking the len of number 
    if len(x.strip()) == 0:
        if cur > best:
            best = cur 
        cur = 0
    else:
        cur = cur + int(x.strip())

print(best) 